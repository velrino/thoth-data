---
name: thoth-catalog-review
description: Review published Thoth company diagrams and studies for walkthrough clarity, visual legibility, and agreement between the story and its data. Use for feedback on an existing diagram or to prioritize a catalog-wide review.
---

# Review Thoth catalog diagrams

Start with the intended audience and the action the diagram teaches. Read `metadata.json` and the workspace or drawing for the requested entry under `content/public/`. Include the locale overlay when reviewing a localized entry. For a catalog-wide review, inventory the scenes first and use the densest or most ambiguous steps to choose browser samples.

## Walk the story

- Start from an observable action, a concrete request, or the main comparison. For cumulative walkthroughs, keep recurring components recognizable through consistent positions, names, roles, and technology marks. Inspect the transition in the browser because camera fit can still change at fixed world coordinates. A deliberate zoom, a distinct subsystem, or a layout that makes the current path easier to follow can justify repositioning. Keep adjacent stages close in focused steps and recheck how the reader returns to the overview.
- Compare the description with the visible edges and ordered flow route. Trace who initiated the action, the checks it passes, the point that permits a success response, and what happens later. Make sure a worker, retry, or optional integration appears at the point the explanation assigns to it.
- At a consequential design choice, ask what the person gains and who pays the cost. Put both in the step where the reader can point to the cause. Resuming an upload saves mobile data, but the service must keep track of incomplete uploads until they finish or expire. For a comparison, use the same example on each path so the reader can explain when each choice makes sense.
- Check for a clear starting point and direction at the default zoom. A focused animated path can teach an ordered transaction. Parallel flows can be useful when concurrency, fan-out, or a comparison is the lesson. Judge whether the simultaneous paths help the reader follow the explanation.
- Prefer short labels that name jobs or outcomes. Check that technical names and caveats are discoverable in component notes or the source panel. Use group names and colors to express meaningful boundaries. A single group around an entire focused scene rarely adds information. For a dense overview, check whether the groups make it easy to see what must finish before the user can continue and what runs afterward, where that distinction applies.

## Check comprehension and 3D readability

- Read the step at its opening zoom with only the visible labels and animation. A first-time reader should be able to say who starts, where the request goes, and what result they get. In a walkthrough, carry one concrete example through the steps when it fits the subject. The overview should also make the most important dependency, trade-off, or failure understandable.
- Follow the main route in reading order. Align consecutive blocks when space allows, reuse adjacent rows for side branches, and prefer a short right-angle turn over a back-and-forth diagonal when it preserves the meaning. Check the actual on-screen spacing after fit. Shorter world coordinates can leave the displayed distances unchanged or increase them. Use groups for distinct responsibilities, stages, or branches.
- Compare the focused scene and the full overview at their default 3D angle. Check that the main path, technology marks, and labels are recognizable without hunting for them. In dense or narrow views, compare 2D and consider introducing the system in stages before the full map. The Google Drive walkthrough is an example of an everyday action and a visible completion boundary. Use different visual structures when the story is about alternatives or concurrent work.
- Mark a broken or misleading main path or an unreadable essential label as a priority. Treat optional polish separately. A reviewer can check the design against these questions, while comprehension by a nontechnical audience requires feedback from an actual reader.

## Verify the scene and renderer

- Run `python3 scripts/validate_catalog.py` from the catalog root. When the host app is available, use its workspace parser or the synced `catalog:check` to verify endpoints, unique IDs within each entity type, and continuous flow routes. Review node and edge ID reuse as a maintainability concern unless you can reproduce a functional failure. Missing labels and changes in component positions are evidence to investigate in context.
- Open the introduction, the densest step, and any transition implicated by the feedback. Check 2D and 3D where offered. Compare desktop and narrow layouts as relevant. Look for tiny logos, hidden labels, collisions between group titles and block labels, ambiguous arrows, and whether a tap or hover reveals a useful label or note. A data check alone cannot confirm visibility.
- Confirm host behavior before recommending a format change. Native edges are directed and can render arrowheads. Connection-label visibility depends on the reference layout and metadata. An original `scene.drawing` uses a separate 2D canvas in the reference viewer. Review it on its own terms rather than expecting it to overlay a native 3D scene. Link to current renderer evidence when attributing a finding to the viewer.
- Keep public claims tied to sources and hypothetical topology recognizable as illustrative. Use the [contribution skill](../thoth-catalog-contribution/SKILL.md) for authorized content changes. Treat camera continuity, label placement, animation scheduling, and new format fields as separately scoped app work when the finding requires it.

Report the affected reference and step, evidence, impact on the reader, and smallest useful correction. State which findings came from the browser and which came from data inspection. Leave content and release state unchanged during a review.
