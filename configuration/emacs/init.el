
;;; Commentary:
;;; package --- Summary
(require 'package)
;;; Code:
(setq package-enable-at-startup nil)
(add-to-list 'package-archives
	     '("melpa" . "https://melpa.org/packages/"))
(package-initialize)

(unless (package-installed-p 'use-package)
	(package-refresh-contents)
	(package-install 'use-package))


(org-babel-load-file (expand-file-name "~/.emacs.d/python.org"))
(org-babel-load-file (expand-file-name "~/.emacs.d/asher.org"))
;;(org-babel-load-file (expand-file-name "~/.emacs.d/lisp.org"))
;;(org-babel-load-file (expand-file-name "~/.emacs.d/noodle.org"))

;; ad-handle-definition: ‘shell’ got redefined
(setq ad-redefinition-action 'accept)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   (quote
    (slime pydoc pycoverage py-autopep8 py-yapf sphinx-doc sphinx-frontend dired+ jedi-direx jedi virtualenvwrapper use-package))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(setq inferior-lisp-program "/usr/local/bin/sbcl")
(setq slime-contribs '(slime-fancy))

(provide 'init)
;;; init.el ends here
