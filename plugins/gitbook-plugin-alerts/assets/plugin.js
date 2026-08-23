require(['gitbook', 'jQuery'], function(gitbook, $) {
  // Default alert types configuration
  var defaultAlerts = {
    note: {
      label: 'Note',
      icon: 'fa fa-info-circle',
      className: 'note'
    },
    tip: {
      label: 'Tip',
      icon: 'fa fa-lightbulb-o',
      className: 'tip'
    },
    warning: {
      label: 'Warning',
      icon: 'fa fa-exclamation-triangle',
      className: 'warning'
    },
    danger: {
      label: 'Danger',
      icon: 'fa fa-ban',
      className: 'danger'
    },
    important: {
      label: 'Important',
      icon: 'fa fa-exclamation-circle',
      className: 'important'
    }
  };

  // Parse inline options like |label:Custom Label|icon:fa fa-star
  function parseOption(options, key, defaultValue, transform) {
    var match = (options || '').match(new RegExp(key + ':([^|\\r\\n]*)'));
    var value = match ? match[1].trim() : defaultValue;
    return transform ? transform(value) : value;
  }

  gitbook.events.bind('page.change', function() {
    var config = gitbook.state.config.pluginsConfig['alerts'] || {};
    
    // Merge user config with defaults
    var alerts = Object.assign({}, defaultAlerts, config);

    $('blockquote').each(function() {
      var $blockquote = $(this);
      var html = $blockquote.html();

      // Match [!TYPE] or [!TYPE|options] pattern (may be inside <p> tags)
      var newHtml = html.replace(
        /<p>\s*\[!(\w+)((?:\|\w+:[^|\r\n]*)*)\]\s*([\s\S]*?)<\/p>([\s\S]*)/gi,
        function(match, type, options, firstContent, restContent) {
          var alertType = type.toLowerCase();
          var alertConfig = alerts[alertType];

          // If not a recognized alert type, return unchanged
          if (!alertConfig) {
            return match;
          }

          // Parse options
          var label = parseOption(options, 'label', alertConfig.label);
          var icon = parseOption(options, 'icon', alertConfig.icon);
          var className = parseOption(options, 'className', alertConfig.className);
          var showIcon = parseOption(options, 'iconVisibility', 'visible', function(v) {
            return v !== 'hidden';
          });
          var showLabel = parseOption(options, 'labelVisibility', 'visible', function(v) {
            return v !== 'hidden';
          });

          // Build the alert HTML
          var iconHtml = showIcon ? '<i class="' + icon + '"></i>' : '';
          var labelHtml = showLabel ? '<span class="label">' + label + '</span>' : '';
          var content = firstContent.trim() + restContent;

          return '<div class="alert alert-' + className + '">' +
                   '<p class="alert-title">' + iconHtml + labelHtml + '</p>' +
                   '<div class="alert-content">' + content + '</div>' +
                 '</div>';
        }
      );

      // Replace blockquote if it was transformed
      if (newHtml !== html) {
        $blockquote.replaceWith(newHtml);
      }
    });
  });
});
