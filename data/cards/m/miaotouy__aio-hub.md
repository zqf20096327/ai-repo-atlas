# miaotouy/aio-hub

⭐ 145 · TypeScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/miaotouy/aio-hub) · [官网](http://aiohub-app.com) · 个人维护 · 中文 README

**本地优先的个人 AI 桌面工作站：人类工具台与 Agent 运行时一体**

基于 Tauri + Vue 3 + TypeScript 的跨平台桌面应用，同时服务人类用户与 Agent：Chat 工作区提供可控上下文管道、74 个宏、上下文压缩与 SillyTavern 世界书/角色卡兼容；人类工作台包含网页蒸馏、窗口自动化、OCR、Git、媒体创作、弹幕播放器等桌面工具；Agent 只能调用显式注册并经审批治理的方法。通过 VCP 协议可作分布式节点或桥接远端工具。原生适配 OpenAI/Anthropic/Gemini/xAI/DeepSeek 等并兼容 Ollama 本地模型。桌面端 Apache-2.0，移动端私有许可，仅供个人学习研究。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一上下文管道：多阶段处理器可视化排序与插件化扩展，附上下文分析器
- Agent 只能调用显式注册且经参数校验、审批、可取消的方法
- VCP 双向互操作：本地能力注册到远端，远端插件桥接为本地工具
- 兼容 SillyTavern 角色卡、正则脚本、快捷动作与世界书

## 适用场景

- 想要高可控 LLM 对话与角色工作流的个人用户本地工作站
- 在明确授权边界内让 Agent 复用本地工具（OCR、网页蒸馏、文件等）
- 将多个 AI 供应商与本地 Ollama 模型集中在一个桌面客户端管理

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L45: AIO Hub 的聊天功能是一个专为复杂任务和深度探索而设计的、高度模块化的**对话式 AI 智能体工作站**。
> L75: - **广泛适配**: 原生支持 OpenAI, Anthropic, Gemini, xAI (Grok), SiliconFlow, DeepSeek, Vertex AI 等，兼容 Ollama 等本地模型。

## 星数曲线

```mermaid
xychart-beta
    title "miaotouy/aio-hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 143 --> 145
    line [144, 144]
```

2026-10-18 144 → 2026-10-28 144（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `729e64eb27da` · [字段定义](../../DATASET.md)*
