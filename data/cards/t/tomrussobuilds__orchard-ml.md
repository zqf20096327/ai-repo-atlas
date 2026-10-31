# tomrussobuilds/orchard-ml

⭐ 14 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/tomrussobuilds/orchard-ml) · 个人维护

**面向计算机视觉研究的 PyTorch 训练框架，YAML 配置驱动可复现实验**

基于 PyTorch 的训练框架，服务可复现的计算机视觉研究：通过单一 YAML recipe 完成图像分类与目标检测训练，配置由 Pydantic V2 校验，支持多分辨率架构（28×28 至 224×224）及 timm 注册表中 1000+ 模型。内置 Optuna 超参搜索（TPE 采样、Median 剪枝、可选模型搜索）、ONNX 导出（含 INT8/UINT8 量化）、MLflow 跟踪、内核级文件锁防止并发冲突、BLAKE2b 哈希的运行目录做审计级溯源。数据以 NPZ 为规范格式；MPS 后端代码存在但未在真实硬件上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 YAML recipe 驱动分类与检测训练，Pydantic V2 类型安全配置
- Optuna 集成超参搜索、剪枝与自动模型搜索
- 默认 ONNX 导出，支持 INT8/UINT8 量化与延迟基准
- BLAKE2b 哈希运行目录 + YAML 快照的实验溯源

## 适用场景

- 用现成 recipe 快速复现视觉分类/检测实验
- 自动搜索超参与架构组合
- 训练后导出量化 ONNX 模型用于边缘部署

## 场景标签

`模型量化` `模型训练` `MLOps` · 领域:训练与推理

## 证据(README 行号)

> L42: **Orchard ML** is a research-grade `PyTorch` training framework engineered for reproducible, scalable computer visi
> L45: - **Type-Safe Configuration Engine**: `Pydantic V2`-based declarative manifests eliminate runtime errors
> L48: - **Intelligent Hyperparameter Search**: `Optuna` integration with TPE sampling and Median Pruning

## 星数曲线

```mermaid
xychart-beta
    title "tomrussobuilds/orchard-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7ff2850a1543` · [字段定义](../../DATASET.md)*
