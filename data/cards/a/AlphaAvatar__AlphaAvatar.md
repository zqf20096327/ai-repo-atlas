# AlphaAvatar/AlphaAvatar

⭐ 823 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/AlphaAvatar/AlphaAvatar) · [官网](https://www.alphaavatar.ai) · 组织维护

**可自托管的全模态实时个人助理框架**

AlphaAvatar 是一个可自托管的全模态个人助理框架，采用插件式实时 Agent 架构，围绕记忆、人格、反思、规划、行为、工具（MCP/RAG/DeepResearch）与虚拟形象七个模块组织。运行时分层包括 RTC 适配器（当前提供 LiveKit 传输）、多模态感知、Agent 执行循环与存储层；支持文本、语音、摄像头与屏幕输入，含说话人与人脸识别、全双工打断。部分模块（Reflection/Planning/Behavior、Character 渲染）状态为 Planned/Pending，远程模型提供商仍需网络与凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 插件式实时 Agent 架构：Memory/Persona/RAG/MCP/Character 等三层插件生态
- 实时多模态输入：文本、语音、摄像头、屏幕观察，支持全双工打断与轮次决策
- 自托管、隐私优先，可运行于自有基础设施
- MCP 工具检索基于 LanceDB 的语义搜索

## 适用场景

- 构建可长期记忆用户偏好与历史的个人助理
- 管理个人笔记与知识库并通过 RAG 检索
- 任务提醒、长期目标拆解与多步工作流规划
- 带语音与虚拟形象的实时交互助手

## 场景标签

`AI 助手` `语音 Agent` `Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L35: AlphaAvatar is a **self-hostable Omni Personal Assistant framework** designed to evolve into an **intelligent perso
> L44: - 🧰 **Tools** through MCP, RAG, DeepResearch, and external integrations
> L57: - **🔌 RTC Adapter**: provides LiveKit transport while keeping the application boundary replaceable; other backends 

## 星数曲线

```mermaid
xychart-beta
    title "AlphaAvatar/AlphaAvatar 星数(近 5 点)"
    x-axis ["2026-10-24", "2026-11-08", "2026-11-16", "2026-11-18", "2026-11-26"]
    y-axis "stars" 818 --> 824
    line [819, 821, 822, 823, 823]
```

2026-10-24 819 → 2026-11-26 823（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `f86b67efc080` · [字段定义](../../DATASET.md)*
