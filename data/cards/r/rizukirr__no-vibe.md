# rizukirr/no-vibe

⭐ 44 · Shell · MIT · 推送 2026-10-29 · [GitHub](https://github.com/rizukirr/no-vibe) · 个人维护

**把 AI 编程助手变成导师的插件：只教不代写，用户自己敲代码**

面向 Claude Code、Codex、opencode、Pi、Antigravity 五种 agent 运行时的插件。启用后通过 hook（block-writes.sh / block-bash-writes.sh）阻止 agent 写入项目文件，agent 仅在对话中教学，代码由用户亲手输入。教学流程分五步：测水平、定目标、生成 .no-vibe/syllabus.md 大纲、讲解、每节至少 3 个练习；可跨会话用 /no-vibe on 恢复进度。守卫非沙箱，基于命令文本模式匹配，README 列出了可绕过的 shell 写法。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- hook 阻止 agent 写项目文件，教学仅发生在对话中
- 五步教学流程：水平→目标→大纲→讲解→练习，大纲存于 .no-vibe/ 可跨会话恢复
- 支持 Claude Code / Codex / opencode / Pi / Antigravity 五种运行时，共用同一守卫脚本
- 提供 /no-vibe-btw 单任务豁免与 /no-vibe-challenge 编码挑战命令

## 适用场景

- 学习新技术时让 AI 编程助手只讲解、自己动手写代码
- 在现有项目中按其技术栈获得贴合项目的学习大纲
- 防止 vibe coding 式的代写，通过练习巩固理解

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: Turn your AI assistant into a teacher. It finds your level, plans what you will learn and shows you code in chat, an
> L9: While no-vibe is on, the agent refuses to write your project files. A hook blocks file tools and shell writes on eve
> L87: |`/no-vibe [on\|off\|<topic>]`|Learning mode. Use ONLY when `.no-vibe/active` exists at the project root or the use

## 星数曲线

```mermaid
xychart-beta
    title "rizukirr/no-vibe 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-30 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `91751a2c6a0e` · [字段定义](../../DATASET.md)*
