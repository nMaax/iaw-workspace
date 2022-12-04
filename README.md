# General Formatting Guidelines

## Format of HTML/Bootstrap files

[Bootstrap docu](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

```html
<always indent>
    <tag class="parent-tag-setup padding border margin child-tag-setup gutter personalClass" id="..." style="..." href/src="..."></tag>
<eventually with some spaces>

<!-- and always remember to comment the various sections and other stuff! -->
<if the innested tag is pretty simple (like p, a, h1, img, ...)> <p></p> <you can eventually skip the indentation>
```

#### The scheme of classes is basically: 
1. Manage how this tag rapports with parent tag (tipically: col, nav-item, ...)
2. Manage the styling of this tag (other, padding, border, margin - in this order)
3. Manage how this tag rapports with child tags (tipically: row, d-flex, ...) 
4. You personal classes
5. For breakpoit use FSTG (From smaller (brekpoint) to greater (breakpoint))
    * class class-sm class-md class-lg class-xl class-xxl
    * When in doubt, always specify the 'obvious' classes like col-12

## Format of CSS files
```css
/* Order of single elements is based on gerarchy since this is a *CASCADE* style sheet */

element {
    parent-display-options: ... ;

    display-type: ... ;
    display-options: ... ;
        columns: ... ;
        rows: ... ;

    width: ... ;
    height: ... ;

    text: ... ;
    font: ... ;
    background: ... ;

    padding: ... ;
    border: ... ;
    margin: ... ;
        top: ... ;
        bottom: ... ;
        right: ... ;
        left: ... ;
 }

```

## Useful tips for VS-CODE

* Always prefer a d-flex option (justify, alig-item, ...) instead of a "manual" padding/margin style
* Should I go for a "manual col handling" or using the col (col-auto) class as the last element whenever is possible?
* Tag.class1.class2.class3*N + TAB for generating N tags (div if tag not specified) with specified classes
```html
<!--e.g.    tag.class1.class2.class3*3 generates:-->
<tag class="class1 class2 class3"></tag>
<tag class="class1 class2 class3"></tag>
<tag class="class1 class2 class3"></tag>
```
* ! + TAB for generating standard html skeleton (doctype and meta viewport included)