# NVIDIA/sop-monitoring-blueprints

⭐ 63 · Python · NOASSERTION · 推送 2026-08-28 · [GitHub](https://github.com/NVIDIA/sop-monitoring-blueprints) · 组织维护

**工业 SOP 视频监控系统的训练与推理微服务及 agentic 技能包**

NVIDIA 维护的标准作业程序（SOP）监控蓝图：包含训练微服务（准备 SOP 专用 VLM 与时序分割模型，支持 Cosmos-Reason/Cosmos3-Nano 微调与 QA 数据生成）和低延迟实时 DeepStream 推理微服务，另有三个面向 AI 编码助手的 agentic 技能包，覆盖微调编排、推理代码生成/评估/基准测试与 VSS 集成部署。面向工业视频场景的开发者，通过自然语言提示驱动完整训练-部署-测试流水线，示例数据为服务器风扇与电源安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 训练微服务生成 QA 训练数据并微调 VLM（Cosmos-Reason/Cosmos3-Nano）与时序分割模型
- DeepStream 实时推理微服务作为参考实现，含评估与延迟基准技能
- agentic 技能包以自然语言提示驱动微调、代码生成、评估与部署
- VSS 技能支持构建/部署/测试四阶段端到端流水线（容器化微服务）

## 适用场景

- 用自有标注视频训练 SOP 监控模型并部署为 API 与 Web 应用
- 通过 AI 编码助手生成与调试 DeepStream 推理微服务
- 在 VSS 上端到端构建并验证 SOP 合规监控流水线

## 场景标签

`微调` `代码生成` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L16: - SOP Fine-tuning Agentic Skills (agentic/sop-agentic-ft/README.md): AI coding assistant skills for fine-tuning SOP
> L17: - DeepStream SOP Agentic Skills (agentic/ds-sop-skills/README.md): AI coding assistant skills for the DeepStream SO
> L61: Two agent-driven paths you can run independently: fine-tune the DDM and Cosmos-Reason models, and generate / evalua

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/sop-monitoring-blueprints 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-26 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `06680c1bfeb7` · [字段定义](../../DATASET.md)*
