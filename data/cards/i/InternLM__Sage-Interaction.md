# InternLM/Sage-Interaction

⭐ 36 · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/InternLM/Sage-Interaction) · 组织维护 · 中文 README

**9B 全双工多模态交互模型，边对话边委派后台任务**

基于 MiniCPM-o 4.5 的 9B 全双工全模态交互模型，可一边持续对话并感知音视频流，一边将任务提交给后台异步执行（需持续推理或工具调用），完成后将结果融入对话。权重发布于 Hugging Face 与 ModelScope。附带实时语音 demo：前端运行本模型、后端连接 OpenAI 兼容 API 执行委派任务；demo 要求 Linux、BF16 NVIDIA GPU、Python 3.12 与 CUDA 12.8。代码与权重均以 Apache 2.0 发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全双工交互：持续感知音视频输入并保持对话连续性（打断/附和/背景语音）
- agentic 任务委派：识别可委派任务异步后台执行，结果回流对话
- 流式视频理解：对实时视频流中事件主动响应
- 基于角色扮演多智能体系统生成场景化交互轨迹用于训练

## 适用场景

- 构建可实时打断的语音交互助手
- 在对话中将耗时任务（旅行规划/科学计算）委派后台执行
- 对实时视频流做主动理解与提醒
- 实验室辅助等科研工作流中的多模态协作

## 场景标签

`语音 Agent` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L34: We introduce **Sage-Interaction**, a **9B-parameter omni interaction model** built on **MiniCPM-o 4.5**. It combine
> L81: The real-time voice demo runs Sage-Interaction as the frontend model and connects to an OpenAI-compatible API as th


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `b0f7cbd4d244` · [字段定义](../../DATASET.md)*
