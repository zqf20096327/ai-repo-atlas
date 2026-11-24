# Picom-code/pico-dgx-ds4

⭐ 159 · Cuda · MIT · 推送 2026-11-20 · [GitHub](https://github.com/Picom-code/pico-dgx-ds4) · 个人维护

**在 4 台 DGX Spark 上运行 DeepSeek V4.1 Flash 的多用户推理引擎**

blaesus/dsgx10 的 fork，针对 4 台 DGX Spark（GB10）通过 RoCE 交换机 TP=4 部署 DeepSeek V4.1 Flash：新增 1M 上下文（17-bit 稀疏注意力块索引）、16 个并发槽位（4 个 1M、12 个 128K，最小适配准入）、图像输入（checkpoint 自带 ViT 作为侧编码器，走 OpenAI 兼容 API），并对单用户与多用户吞吐做了多项优化（stack4/stack5）。运行需 4 台 GB10 主机与 ConnectX-7 链路，按上游目录的构建说明部署。README 给出大量自行测得的吞吐与基准对比数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1M 上下文与 16 并发槽位（4×1M + 12×128K，最小适配准入）
- 图像输入经 OpenAI 兼容 API（image_url），ViT+aligner 侧编码器约占 1GB 显存
- stack5 去中继集合通信：RoCE 交换机下各节点直写全对等节点
- 提供与上游及 SGLang kit 的同机同日对比基准数据

## 适用场景

- 在 4 台 DGX Spark 集群上多人共享同一 DeepSeek 服务
- 长上下文（至 1M）本地推理与代理式工作负载
- 通过 OpenAI 兼容 API 接入含图像的多模态请求

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: pico-dgx-ds4: DeepSeek V4.1 Flash on 4x DGX Spark
> L88:   1  hardware ....... 4x DGX Spark (GB10, 128 GB), ConnectX-7 links. We run TP4 through a 200G RoCE
> L125: From-scratch inference engines for NVIDIA GB10 boxes.

## 星数曲线

```mermaid
xychart-beta
    title "Picom-code/pico-dgx-ds4 星数(近 11 点)"
    x-axis ["2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 101 --> 157
    line [105, 109, 112, 119, 124, 131, 135, 150, 151, 153, 153]
```

2026-11-13 105 → 2026-11-24 153（+48）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `28347e03cecb` · [字段定义](../../DATASET.md)*
