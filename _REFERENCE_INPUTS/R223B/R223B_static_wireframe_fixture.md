# R223B Static Wireframe Fixture

This fixture shows how R223B applies the static wireframe spec to R223A-P1 component slots. It is not UI code.

## Fixture 1: 有趣的纸印 / 材料与印痕探究

```text
Mode: daily_prep
Focused Section: 材料与印痕探究
Student Problem: 学生不清楚纸材、按压和工具如何影响印痕。
Teacher Visible Reason: 这组组件先让学生试材料，再看关键步骤，最后留下试印证据。
Visible Component Count: 3 / limit 3
Component Strip:
- material_mystery_box
- technique_step_demo
- learning_sheet_record
Media Summary: 3-5种纸材或替代材料; 滚印/拓印步骤图或短视频; 试印记录学习单
Evidence Summary: 试印小样; 材料效果记录; 步骤核对或错误修正
Screen Prompt Summary: 材料盲盒：摸特点，试效果。; 技法拆解：看步骤，试一次。
Teacher Actions: confirm_component_group, replace_one_component, delete_optional_component
```

## Fixture 2: 有趣的文字和图画 / 文字图像关系观察

```text
Mode: daily_prep
Focused Section: 文字图像关系观察
Student Problem: 学生容易把课上成识字或装饰字，不能说明文字和图画如何互相帮助。
Teacher Visible Reason: 这组组件用对比、圈注和匹配把“字形-图像-字义”的关系显性化。
Visible Component Count: 3 / limit 3
Component Strip:
- compare_two_images
- circle_and_annotate
- match_cards
Media Summary: 2张有差异的字卡; 可圈注字形图; 象形字/字义/图画提示卡
Evidence Summary: 圈注位置; 图文关系说明; 匹配理由
Screen Prompt Summary: 比一比：找差异，说依据。; 圈一圈：圈关键处，写理由。
Teacher Actions: confirm_component_group, replace_one_component, delete_optional_component
```

## Fixture 3: 会说话的手 / 手势观察与视觉转译

```text
Mode: daily_prep
Focused Section: 手势观察与视觉转译
Student Problem: 学生可能只表演，不留下手势、线稿、手印角色等视觉证据。
Teacher Visible Reason: 这组组件先标出手势表达依据，再拆解手印角色方法，最后收过程图证据。
Visible Component Count: 3 / limit 3
Component Strip:
- circle_and_annotate
- technique_step_demo
- photo_submit
Media Summary: 手势图片或暂停帧; 手印角色步骤图; 拍照提交节点
Evidence Summary: 手势圈注图; 半成品步骤照片; 最终手印角色
Screen Prompt Summary: 圈一圈：圈关键处，写理由。; 拍照提交：拍证据，写看点。
Teacher Actions: confirm_component_group, replace_one_component, delete_optional_component
```

## Fixture 4: 美术大家庭 / 生活中的美术门类连接

```text
Mode: quick_prep
Focused Section: 生活中的美术门类连接
Student Problem: 学生只背门类名称，不能把校园和生活例子连到美术大家庭。
Teacher Visible Reason: 快速稿只保留关系匹配和最小证据记录，避免增加课堂负担。
Visible Component Count: 2 / limit 2
Component Strip:
- match_cards
- learning_sheet_record
Media Summary: 校园或生活图片卡; 门类名称卡; 一格关系记录
Evidence Summary: 一条图片-门类连线; 一个生活用途理由
Screen Prompt Summary: 连连看：连图、连词、连理由。
Teacher Actions: confirm_component_group, delete_optional_component
```

## Fixture 5: 有趣的纸印 / 保底可上课试印链

```text
Mode: quick_prep
Focused Section: 保底可上课试印链
Student Problem: 快速备课时容易只写材料和步骤，漏掉印痕证据底线。
Teacher Visible Reason: 快速稿只保留关键技法和最小试印证据，保证明天能上。
Visible Component Count: 2 / limit 2
Component Strip:
- technique_step_demo
- learning_sheet_record
Media Summary: 关键步骤图或教师现场示范; 试印记录栏
Evidence Summary: 一条试印记录; 一个步骤提醒
Screen Prompt Summary: 技法拆解：看步骤，试一次。
Teacher Actions: confirm_component_group, delete_optional_component
```
