# Theodora-Y/MaskClaw

⭐ 13 · Python · 推送 2026-09-26 · [GitHub](https://github.com/Theodora-Y/MaskClaw) · [官网](https://arxiv.org/abs/2605.28646) · 组织维护 · 中文 README

**端侧 Agent 的隐私守卫层：本地识别敏感信息并脱敏拦截**

面向 OpenClaw、AutoGLM 等端侧 Agent 的隐私防护框架：通过 Hooking 机制在 Agent 执行操作前介入，经 PII 检测、RAG 规则检索（ChromaDB）与端侧模型（MiniCPM-V 4.5/Gemma 4）语义推理，输出 Allow/Block/Mask/Ask/Unsure 五级判决，并用 RapidOCR+OpenCV 做本地视觉打码。规则从用户行为中抽取、沙盒验证后挂载，随使用自进化。支持企业级（服务器 GPU）与个人（CPU）两种部署，附 622 条评测数据集 P-GUI-Evo 与论文。以 FastAPI 服务形式安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent 执行前介入的感知-认知-执行-进化四层架构
- 五级置信度判决（Allow/Block/Mask/Ask/Unsure）人机协作机制
- 基于用户行为自进化规则抽取，沙盒验证后自动挂载
- 全端侧推理，数据不出设备；附 P-GUI-Evo 评测数据集

## 适用场景

- 手机端 Agent 操作前的隐私拦截与截图脱敏
- 企业移动办公场景防止敏感信息经 Agent 外流
- 医疗、金融等数据不出端的合规场景做本地隐私判决

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L32: **MaskClaw** 是专为这类 Agent 设计的隐私守卫层——在 Agent 执行操作前介入，判断这个动作该不该做、该怎么做，且所有推理全部在设备本地完成，**数据不出端**。
> L40: **MaskClaw** 是一个面向**端侧 Agent 隐私保护**的**自进化规则抽取框架**。它并非传统的数据加密或内容过滤工具，而是在 Agent 执行操作前进行**过程内调节**：识别敏感信息、判断操作风险、智能脱敏，并
> L107: |**Layer 1**|感知层 (Perception)|RapidOCR 格式敏感识别、OpenCV 本地视觉模糊处理|

## 星数曲线

```mermaid
xychart-beta
    title "Theodora-Y/MaskClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `31d8c38ed27a` · [字段定义](../../DATASET.md)*
