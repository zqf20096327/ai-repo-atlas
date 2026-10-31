# nanbo0ne/O.R.C.A-for-Windows

⭐ 14 · Go · MIT · 推送 2026-09-23 · [GitHub](https://github.com/nanbo0ne/O.R.C.A-for-Windows) · [官网](https://orca-agent.io) · 个人维护 · 中文 README

**面向真实工作的开源 AI 工作区：对话、编程、研究与办公产物一体**

基于 Wails 的桌面 AI 工作区，提供三种模式：ORCA Agent（会话派发与自动化）、助手（问答、调研、办公任务）、编程（Shell/Git/LSP/CodeGraph 等工程工具）。支持多 Provider（DeepSeek、OpenAI/Anthropic-compatible 自定义接入），内置 MCP、Skill、subagent、产物工具（DOCX/XLSX/PPTX/PDF）、记忆与权限策略。3.0.13 在所有平台暂时禁用托管 llama.cpp 本地 AI 与 Computer Use，外部本地服务仍可手动配置。Windows/macOS/Linux 提供安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种工作模式：ORCA Agent / 助手 / 编程，工具与记忆按模式隔离
- MCP（stdio 与 Streamable HTTP）、Skill、subagent 与 QQ/微信/飞书机器人渠道
- 面向 DOCX/XLSX/PPTX/PDF 的 artifact 工具链与结构化 sidecar
- 托管 llama.cpp 本地 AI 与 Computer Use 在 3.0.13 全平台暂时禁用

## 适用场景

- 在统一桌面应用里完成问答、调研与日常办公任务
- 用编程模式进行仓库开发、调试与代码审查
- 通过 MCP 与 Skill 扩展助手能力并接入机器人渠道
- 生成并校验 Office/PDF 办公产物

## 场景标签

`编码 Agent` `代码审查` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L5: **O.R.C.A.**（**Open Reasoning & Computing Agent**）是面向真实工作的开源 AI 工作区：把模型对话、助手、编程、研究、文件与图片、工程工具、记忆和自动化放在同一个可暂停、可检查、可恢复
> L30: |**ORCA Agent**|跨会话协调、机器人渠道、长期入口|处理会话派发、等待和自动化；不是普通文本子代理的替代品|
> L31: |**助手**|问答、调研、写作、资料整理、办公文件和日常任务|使用联网/本地工具、助手记忆、计划、自动化和产物工具|
> L32: |**编程**|仓库开发、调试、重构、测试、审查|使用 Shell、文件、Git、LSP、CodeGraph、检查点和工程验证|

## 星数曲线

```mermaid
xychart-beta
    title "nanbo0ne/O.R.C.A-for-Windows 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `3fe075b48dfb` · [字段定义](../../DATASET.md)*
