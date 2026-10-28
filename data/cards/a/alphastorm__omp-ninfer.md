# alphastorm/omp-ninfer

⭐ 46 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/alphastorm/omp-ninfer) · [官网](https://alphastorm.github.io/omp-ninfer/) · 个人维护

**把 Oh My Pi 编码代理接入本地 Qwen3.8 27B 的可复现推理套件**

面向持有 RTX 3090/4090/5090 的 Windows 11 单机用户的本地推理交付层：将编码代理 Oh My Pi 与 NInfer（C++/CUDA 推理引擎）及一个哈希锁定的 Qwen3.8 27B 模型绑定，通过有状态 OpenAI Responses 接口提供重启后可恢复的会话延续，检查点在服务器重启后还原。双端点仅绑定环回、请求带 bearer 认证、模型回退关闭（GPU 不可达即失败）。发布以 manifest 绑定模型 SHA-256、容器摘要/SBOM 与各通道验收回执，可用脚本校验克隆即合格发布。限制：单一模型、单一本机所有者、通道各有吞吐与并发限制，检查点仅在相同运行时/模型/配置下还原。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 有状态 OpenAI Responses（previous_response_id）延续 + 重启后检查点还原
- 环回绑定、bearer 认证、fail-closed 无云端回退
- manifest 绑定模型 SHA-256/容器摘要/SBOM 与验收回执，可脚本校验
- 三条 GPU 通道（RTX 3090/4090/5090）各带实测吞吐与检索数据

## 适用场景

- 在自有 GPU 上私密运行 Oh My Pi 长编码会话，不把代码发往云端
- 服务器重启后继续之前的编码会话而不丢失状态
- 按已验收的硬件/软件组合获得可复现的本地推理部署

## 场景标签

`推理引擎` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L87: Oh My Pi (coding-agent client) → OMP NInfer (qualified appliance and release layer) → NInfer
> L92: - **NInfer owns inference and retained state.** The C++/CUDA engine from
> L29: - **Explicit and durable.** Oh My Pi drives NInfer through stateful OpenAI Responses

## 星数曲线

```mermaid
xychart-beta
    title "alphastorm/omp-ninfer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-28 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bd6174a610d4` · [字段定义](../../DATASET.md)*
