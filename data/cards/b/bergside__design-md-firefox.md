# bergside/design-md-firefox

⭐ 16 · JavaScript · MIT · 推送 2026-04-24 · [GitHub](https://github.com/bergside/design-md-firefox) · [官网](https://addons.mozilla.org/en-US/firefox/addon/design-md/) · 个人维护

**从任意网站提取样式并生成 DESIGN.md/SKILL.md 的 Firefox 扩展**

Firefox 浏览器扩展：读取当前标签页的排版、颜色、间距、圆角、阴影、动效等样式信号，基于开源 TypeUI DESIGN.md 格式生成设计系统文档 DESIGN.md 或面向 agent 的 SKILL.md，供 Google Stitch、Claude Code、Codex 等工具在设计蓝图约束下构建网站。生成的文件包含 Mission、Brand、Style Foundations、WCAG 2.2 AA 可访问性要求、Do/Don't 规则与质量门等章节。以临时加载未签名扩展方式安装，公开发布需经 AMO 打包签名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从活动标签页自动提取 typography/colors/spacing/radius/shadows/motion 样式
- 生成 DESIGN.md 与 agent 可用的 SKILL.md 两种输出
- 生成内容含 WCAG 2.2 AA 可访问性要求与可测试的质量门
- 提供 Explain（?）功能说明文件生成方式

## 适用场景

- 把我喜欢的网站样式提取成设计蓝图交给 AI 编码工具复刻
- 为 Claude Code/Codex 等 agent 准备 SKILL.md 设计技能文件
- 将现有站点的设计系统文档化为实现规范

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: This Firefox extension extracts styles and information from a given site and generates a `DESIGN.md` or `SKILL.md` f
> L26: |Auto-extract|Reads styles from the active tab (typography, colors, spacing, radius, shadows, motion).|
> L28: |Generate `SKILL.md`|Produces agent-ready skill markdown from extracted signals.|

## 星数曲线

```mermaid
xychart-beta
    title "bergside/design-md-firefox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9def8386182e` · [字段定义](../../DATASET.md)*
