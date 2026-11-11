# Hero review

Judge the actual rendered interface and the user's brief, not whether fashionable effects appear.

## Composition and credibility

- The hero has a dominant focal point and a composition chosen for this product. It has not slipped into the prohibited default text/image split.
- The visual could not be reused unchanged for an unrelated industry. Copy, assets, and interactions convey the real offering.
- No invented metrics, customers, testimonials, logos, credentials, or interface capabilities are presented as real.
- Distinctiveness survives implementation: the chosen layout, media role, type, and rhythm still match the direction contract.
- The headline, supporting copy, and action remain understandable. Decoration does not obscure the message.

## Site coherence and assets

- Adjacent requested sections share font roles, color roles, spacing, image treatment, and motion behavior. Each does not look like a different library demo.
- Headline wraps are intentional at desktop and mobile widths. Body copy is readable, and fonts actually load with usable fallbacks.
- Images retain believable geometry, detail, and lighting; generated artifacts are corrected or replaced. Key subjects survive mobile cropping.
- Controls and essential text are live UI. Required placeholders or missing assets are disclosed, not called finished.

## Behavior and technical fit

- Inspect desktop and narrow mobile renders together. Check overflow, crop, action visibility, overlaps, and nav behavior; add an intermediate width only if the layout warrants it.
- Exercise the primary action and any introduced controls. Check keyboard focus, semantic order, accessible names, contrast, touch use, and reduced-motion behavior.
- When motion changed, verify entrance/replay behavior, forward and backward scrolling, resize refresh, route cleanup, and the complete reduced-motion state. Confirm ScrollTrigger markers are absent from the shipped result.
- Check hero loading, media dimensions, and expensive animation. Keep static fallbacks useful and avoid unnecessary work when media is offscreen.
- Verify the changed code using relevant project checks. Investigate review-tool findings against source and rendered evidence before making changes.

Use one batched inspection, one batch of fixes, and at most one confirmation pass unless a newly discovered functional failure needs further repair. Report any unverified behavior accurately.
