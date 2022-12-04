# GENERAL FORMATTING GUIDELINES

## FORMAT OF HTML-BOOTSTRAP FILES

```html
<always indent>
    <tag class="parent-tag-setup padding border margin child-tag-setup gutter personalClass" id="..." style="..." href/src="..."></tag>
<eventually with some spaces>

<if the innested tag is pretty simple (like p, a, h1, img, ...)> <p></p> <you can eventually skip the indentation>
<!-- and always remember to comment the various sections and other stuff! -->
```

#### The scheme of classes is basically: 
    1. Manage how this tag rapports with parent tag (tipically: col, nav-item, ...)
    2. Manage the styling of this tag (other, padding, border, margin - in this order)
    3. Manage how this tag rapports with child tags (tipically: row, d-flex, ...) 
    4. You personal classes
    5. For breakpoit use FSTG (From smaller (brekpoint) to greater (breakpoint))
        * class class-sm class-md class-lg class-xl class-xxl
        * When in doubt, always specify the 'obvious' classes like col-12

## FORMAT OF CSS-STYLE SHEET
```css
/* Order of single elements is based on gerarchy since this is a *CASCADE* style sheet */

element {
    parent-display-options: ;

    display-type: ;
    display-options: ;
        columns: ;
        rows: ;

    width: ;
    height: ;

    text: ;
    font: ;
    background: ;

    padding: ;
    border: ;
    margin: ;
        top: ;
        bottom: ;
        right: ;
        left: ;
 }

```

## BOOTSTRAP QUICK-ACCESS DOCU

* Bootstrap doc: https://getbootstrap.com/docs/5.2/getting-started/introduction/

* Layouts: https://getbootstrap.com/docs/5.2/layout/breakpoints/
    * Gutters: https://getbootstrap.com/docs/5.2/layout/gutters/
    * Images: https://getbootstrap.com/docs/5.2/content/images/

* Content: https://getbootstrap.com/docs/5.2/content/reboot/
    * Typography: https://getbootstrap.com/docs/5.2/content/typography/

* Utilites: https://getbootstrap.com/docs/5.2/utilities/api/
    * Margin and Pagging: https://getbootstrap.com/docs/5.2/utilities/spacing/#margin-and-padding
    * Borders: https://getbootstrap.com/docs/5.2/utilities/borders/#border
    

## TIPS IN VS-CODE

* always prefer a d-flex option (justify, alig-item, ...) instead of a "manual" padding/margin style

* should I go for a "manual col handling" or using the col (col-auto) class as the last element whenever is possible?

* tag.class1.class2.class3*N + TAB for generating N tags (div if tag not specified) with specified classes

    e.g.    tag.class1.class2.class3*3
    ```html
        <tag class="class1 class2 class3"></tag>
        <tag class="class1 class2 class3"></tag>
        <tag class="class1 class2 class3"></tag>
    ```

* ! + TAB for generating standard html skeleton (doctype and meta viewport included)