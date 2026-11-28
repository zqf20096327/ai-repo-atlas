# nateGeorge/mlx-abliterate

⭐ 3 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/nateGeorge/mlx-abliterate) · 个人维护

**在 Apple Silicon 上原生运行 MLX 拒绝方向消融的工具**

在 MLX 上原生实现拒绝方向消融（abliteration，Arditi et al. 2024），无需 PyTorch、transformers 建模代码或租用 GPU。流程分五步：捕获残差流、由配对有害/无害提示计算拒绝方向、从各层输出投影中移除该方向、字符串级拒绝评分、对未修改模型计算 KL 散度。量化模块按自身 group size 原地去量化-投影-重量化。README 附 Recursive Flint 40B-A2.5B 的实测结果与限制说明（评分器为字符串匹配、仅消融残差流方向等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MLX 原生实现，不依赖 PyTorch 或 transformers
- 量化模块原地去量化-投影-重量化
- 五步流程：capture/directions/ablate/score/KL
- 发布配置与实测数据表（基线拒绝率 46.2%/44.2% → 13.5%）

## 适用场景

- 在 Apple Silicon Mac 上对 MLX 格式模型执行拒绝方向消融
- 为只有 MLX 实现而无 transformers 实现的架构做消融
- 以网格扫描选层带与强度并评估 KL 代价

## 场景标签

 · 领域:LLM/模型修改工具

## 证据(README 行号)

> L3: Abliteration (refusal-direction ablation, Arditi et al. 2024)
> L4: implemented natively in **MLX**, so it runs on Apple Silicon without PyTorch,
> L15: 1. **Capture** — replay the model's own forward pass with each decoder layer


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `171b2719d0cd` · [字段定义](../../DATASET.md)*
