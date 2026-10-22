# NVIDIA/asset-harvester

⭐ 271 · Python · Apache-2.0 · 推送 2026-09-09 · [GitHub](https://github.com/NVIDIA/asset-harvester) · 组织维护

**从驾驶日志提取仿真用 3D 高斯资产生成模型（NVIDIA）**

NVIDIA 发布的生成式 AI 模型与端到端流水线：将真实驾驶日志中稀疏、部分遮挡的物体观测（车辆、行人、骑行者等）转换为完整可仿真的 3D Gaussian Splat 资产。机制上由 SparseViewDiT 多视角扩散模型生成一致新视角，再经前馈 Gaussian 重建器在数秒内生成 3D；管线接入 NVIDIA NCore 与 NuRec 用于闭环仿真数据生成。支持微调（全量或 LoRA）与基准评测（PSNR/LPIPS/SSIM 等）。需 NVIDIA GPU（约 16GB VRAM）、conda 环境，检查点从 Hugging Face 下载；声明仅面向 AV 领域，其他领域结果不保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多视角扩散 + Gaussian lifting 从单视角/稀疏视角生成完整 3D 资产
- 输出可直接插入仿真环境的 3D Gaussian Splat 资产与 metadata.yaml
- 接入 NVIDIA NCore/NuRec 管线，支持闭环仿真数据生成
- 提供微调（LoRA/全量）与渲染评测基准（PSNR/LPIPS/SSIM/DINOv3）

## 适用场景

- 把采集的驾驶场景日志转成可复用 3D 资产，免去手工建模
- 为自动驾驶闭环仿真批量生成高保真物体资产
- 在自有解析样本上微调 SparseViewDiT 多视角扩散模型

## 场景标签

`微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: NVIDIA Asset Harvester is a generative AI model that extracts 3D Gaussian object representations directly from captu
> L19: **Asset Harvester** turns real-world driving logs into complete, simulation-ready 3D assets — from just one or a fe

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/asset-harvester 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 267 --> 272
    line [268, 269, 271]
```

2026-10-18 268 → 2026-10-22 271（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `7839290c27d5` · [字段定义](../../DATASET.md)*
