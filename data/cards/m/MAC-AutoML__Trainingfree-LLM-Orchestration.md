# MAC-AutoML/Trainingfree-LLM-Orchestration

⭐ 16 · Python · 推送 2026-05-16 · [GitHub](https://github.com/MAC-AutoML/Trainingfree-LLM-Orchestration) · 组织维护

**免训练的 LLM 编排框架：组合现成模态专家构建全能交互助手**

ICML 2026 论文的参考实现仓库：通过组合现成的 LLM、视觉、ASR、TTS 专家构建交互式全能模态助手，不做端到端多模态对齐训练。机制分三层——LLM 控制器发出显式控制令牌选择与调度专家、以文本为中心的跨模态记忆压缩多模态证据供跨轮复用、交互运行时执行全双工流式交互与语音打断。各专家经 .env 配置 API 端点与密钥接入，可独立替换升级。提供 GUI 与 CLI 入口，用 uv 管理安装。面向多模态助手方向的研究者与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免训练组合 LLM/视觉/ASR/TTS 现成专家，无需梯度对齐
- LLM 控制器发出显式可审计控制令牌做专家路由
- 文本中心跨模态记忆，跨轮复用已有多模态证据
- 全双工流式运行时：语音打断、实时视频定位、模态一致切换

## 适用场景

- 构建可打断、全双工流式的语音视频交互助手
- 研究免训练的多模态专家编排与路由机制
- 通过配置文件独立替换/升级各模态专家组件

## 场景标签

`多模态` `语音 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L30:  🚀 A training-free orchestration framework for building interactive omni-modal assistants by composing off-the-shel
> L69: LLM Orchestration separates multimodal assistant construction into three coordinated layers:
> L75: |**Interaction Runtime**|Executes ASR, video capture, LLM calls, TTS playback, streaming responses, and interruptio

## 星数曲线

```mermaid
xychart-beta
    title "MAC-AutoML/Trainingfree-LLM-Orchestration 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `75b858f3523c` · [字段定义](../../DATASET.md)*
