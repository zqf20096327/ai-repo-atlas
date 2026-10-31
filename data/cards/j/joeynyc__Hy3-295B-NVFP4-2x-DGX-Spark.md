# joeynyc/Hy3-295B-NVFP4-2x-DGX-Spark

⭐ 14 · Shell · MIT · 推送 2026-07-07 · [GitHub](https://github.com/joeynyc/Hy3-295B-NVFP4-2x-DGX-Spark) · 个人维护 · 中文 README

**在 2 台 DGX Spark 上部署 Hunyuan 3 295B 的 vLLM 配置与脚本集**

面向自建部署的工程仓库：用 vLLM + Ray 在两台 DGX Spark（GB10）上以 TP=2 经 200 GbE RoCE 服务腾讯混元 3 295B MoE（21B 激活，NVFP4 量化权重约 158 GB）。默认配置经过逐项 A/B 基准（TP 对比 PP、TurboQuant k8v4 KV 缓存、关闭 MTP 投机解码等），实测单流约 26 tok/s、256K 上下文。提供 start/stop 脚本、三种 serve profile、hy3ctl 状态与基准工具及终端聊天客户端，并附带故障排查表。限制：需 2× DGX Spark、Docker、每节点约 180 GB 磁盘，冷加载约 10 分钟。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TP=2 部署配置，实测单流 ~26 tok/s、4 并发聚合 60 tok/s
- 三种 serve profile（256K 默认/64K 多用户/PP=2 参照），含基准与 A/B 决策记录
- hy3ctl 状态检查与确定性基准脚本、hy3chat 终端聊天客户端
- 包含两个 vLLM 上游修复贡献及本仓库内的 mod 补丁

## 适用场景

- 我在两台 DGX Spark 上自建 Hunyuan 3 295B 推理服务
- 我需要 256K 长上下文或并发 agent 流量的本地部署配置
- 我想复现或参照该硬件组合上的调优基准数据

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: Serve **Tencent Hunyuan 3 (295B MoE, 21B active)** across two DGX Spark (GB10) nodes with vLLM + Ray — tuned, benchm
> L71: ./start.sh              # containers on both nodes → Ray → mods → vLLM → wait → bench

## 星数曲线

```mermaid
xychart-beta
    title "joeynyc/Hy3-295B-NVFP4-2x-DGX-Spark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2f1b2f706f2b` · [字段定义](../../DATASET.md)*
