# rtmandreyev/construct

⭐ 18 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/rtmandreyev/construct) · [官网](https://rtmandreyev.github.io/construct/) · 个人维护

**让任意 AI agent 从自然语言生成全息 3D 模型及部件的技能与 MCP 工具**

面向 AI agent 的 3D 构建工具链：agent 依据用户文字请求编写纯数据格式的 scene 文件（事实、部件、装配关系），Construct 校验（悬浮部件、证据不足的声明等）并生成单文件 construct.html 全息动画页面，可导出带命名部件与关节的 glTF 供 Blender、游戏引擎使用。以 Claude Code/Hermes 技能、MCP server、OpenAI 兼容 CLI 三种方式接入，masterpiece 模式由独立 critic 多轮评审。仅依赖 Python 标准库与浏览器，可无模型手工运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- scene 为纯数据，agent 不写图形代码，Construct 决定呈现
- 每项事实与部件标注 verified/supplied/inferred/decorative 来源
- 产物为单文件离线 HTML 全息动画，另可导出 glTF（Blender 插件）
- MCP client、OpenAI 兼容端点、Claude Code/Hermes 技能均可接入，无需系统级安装

## 适用场景

- 让 AI agent 为游戏生成带命名部件与关节的 glTF 道具或 blockout
- 把 NetLogo 仿真运行记录渲染为可回放的 3D 构造
- 制作按音乐节奏装配并输出视频的动效片段
- 为博物馆/教学制作标注证据来源的重建模型

## 场景标签

 · 领域:3D 生成/Agent 工具链

## 证据(README 行号)

> L35: - **Any agent, any model.** Claude Code, Hermes, any MCP client or any OpenAI-compatible endpoint, or by hand.
> L134: |Any MCP client|Add `{"mcpServers": {"construct": {"command": "python3", "args": ["/path/to/construct/construct_ho
> L61: 3. **The agent writes a scene.** A scene is a short text file that says what the thing is: the


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bcebd84bfba6` · [字段定义](../../DATASET.md)*
