# mrw7/three-studio

⭐ 3 · JavaScript · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/mrw7/three-studio) · 个人维护 · 中文 README

**开发者用对话生成 Three.js 3D 场景的本地工作台**

本地优先的 Three.js 3D 工作台：AI 通过工具编写自包含场景代码，在沙盒 iframe 中渲染预览，同一界面集成编辑器、时间线、dope sheet、拍摄、审阅标记、测量、资产、会话与插件市场。自带 Node 服务器、存储与 agent 循环，依赖 Node 24，React 与 Three.js 为 vendored，无需包安装。内置 DeepSeek，可添加任意 OpenAI/Anthropic 兼容 provider；数据存于 ~/.three-studio，仅绑定 loopback，不发送遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 通过流式工具调用编写并修订 Three.js 场景，代码仅运行于 opaque-origin srcDoc 沙盒
- 导出 PNG、确定性 MP4/GIF、WebM、glTF/glB、STL、OBJ、USDZ、FBX 7.4、项目 ZIP 与独立 HTML
- 插件市场提供 20 个一键安装模块（skills、深研、MCP 连接器、浏览器自动化等）
- 本地优先存储：会话/场景/凭据存于 ~/.three-studio，仅绑定 loopback 且无遥测

## 适用场景

- 通过对话快速生成并迭代 Three.js 交互场景
- 制作带交互手册与多机位短片的产品演示
- 在本地离线环境中运行 3D 制作与导出流程

## 场景标签

`代码生成` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L6: Three Studio turns a conversation into a live 3D workspace. The AI writes
> L7: self-contained Three.js scenes through tools, the preview renders them in a
> L49: - **Bring your own model** — DeepSeek is built in; add, edit or delete any
> L50:  OpenAI-compatible or Anthropic-compatible provider with its own API key, base


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `c9e32a024dfe` · [字段定义](../../DATASET.md)*
