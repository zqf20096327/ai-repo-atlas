# adithyanraj03/Qwen-3.8-Local-Benchmark

⭐ 6 · HTML · NOASSERTION · 推送 2026-11-24 · [GitHub](https://github.com/adithyanraj03/Qwen-3.8-Local-Benchmark) · 个人维护

**7 个 Qwen3.8 本地构建在 54 项真实任务上的基准报告**

对 7 个 Qwen3.8 本地构建逐一运行同一组 54 项手动任务（游戏/3D、SVG/着色器、Web 应用、C++/Rust/Go、重构、LaTeX 等），共 378 次运行，全部在一台 RTX 5090 + 64 GB 内存机器上完成并人工评分。评分按视觉、提示遵循、输出、创造性、代码五个维度，附逐项扣分说明。结果以静态站点发布：排行榜、每轮视频录制、会话日志、可浏览器试玩的 demo 及 CSV/JSON 原始数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个构建 × 54 项任务共 378 次运行，逐轮录制与人工评分
- 五维评分（视觉/提示遵循/输出/创造性/代码）并公开逐项扣分理由
- 每轮运行的会话日志与引擎启动参数（含 KV cache、上下文窗口配置）
- 原始数据以 CSV/JSON 提供，站点为纯静态页面

## 适用场景

- 对比本地 Qwen3.8 各构建在编码与创意任务上的表现
- 查看模型在实际任务中的录屏与可试玩 demo
- 下载逐轮评分数据做自己的分析

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # Qwen3.8 local model benchmark — 7 builds, 54 real tasks
> L11: Seven Qwen3.8 builds, each run alone through the same 54 hands-on tasks: games and 3D worlds, SVG and shaders, web 
> L13: **Live report:** adithyanraj03.github.io/Qwen-3.8-Local-Benchmark. Scores, recordings, notes and playable demos for


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `28b4574f1ff8` · [字段定义](../../DATASET.md)*
