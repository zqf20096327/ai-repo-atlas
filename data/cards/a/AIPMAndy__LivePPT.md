# AIPMAndy/LivePPT

⭐ 79 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/AIPMAndy/LivePPT) · 个人维护 · 中文 README

**把 Markdown/README 一条命令生成可翻页 HTML 演示页的工具**

由个人开发者维护的演示页生成器：输入 Markdown 或 README，通过 make 命令（build-from-readme / build-showcase）与 Python 脚本（render_plan_to_html.py、add_theme.py）生成单文件 HTML 演示页，支持翻页、导航点、进度条、键盘控制及主题/品牌参数切换；网页首页无需 Node.js 构建。自述为 MVP，尚不支持任意 README 无损高保真转换与复杂布局识别。仓库内含 SKILL.md，可作为 Claude 类 agent 技能使用；根目录与 Skill 目录存在两份不同许可文本（Apache-2.0 与 MIT 附加条款），商用需先确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- README/Markdown 直接生成单文件 HTML deck
- build-showcase 一条命令生成内容与 HTML
- 支持主题切换、品牌名、封面副标题参数
- 翻页、导航点、进度条、键盘控制
- 提供 SKILL.md 供 agent 框架调用

## 适用场景

- 开源项目把 README 变成可分享的演示页
- 产品发布快速产出可讲解的网页演示
- 同一内容切换不同视觉风格用于售前
- 课程讲义拆成节奏化翻页页面

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L76: - `build-from-readme`：README 直接生成 HTML deck
> L78: - `render_plan_to_html.py`：把 Markdown 渲染为单文件 HTML deck
> L118: - 技能定义：`skills/public/LivePPT/SKILL.md`

## 星数曲线

```mermaid
xychart-beta
    title "AIPMAndy/LivePPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-26 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `89e642a31362` · [字段定义](../../DATASET.md)*
