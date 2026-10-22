# Project-MONAI/monai-deploy-app-sdk

⭐ 144 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/Project-MONAI/monai-deploy-app-sdk) · 组织维护

**医疗影像 AI 推理应用的开发打包框架**

面向医疗影像领域的 Python 框架，用于设计、开发与验证 AI 推理应用：通过 DAG 组织推理流程，内置 DICOM 数据加载算子，支持进程内 PyTorch 推理与经 Triton Inference Server 的远程推理，可用单条命令将应用打包为 MONAI Application Package，并用 App Runner 本地运行调试。核心依赖 NVIDIA Holoscan SDK（CUDA 13），要求 Ubuntu 22.04、CUDA 13.0+ 及至少 8GB 显存的 NVIDIA GPU，Python 3.10-3.13。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以可编程 DAG 管理推理应用流程
- 内置 DICOM 加载算子与 MONAI 前后处理变换集成
- 支持进程内 PyTorch 推理与 Triton Inference Server 远程推理
- 单命令打包为 MONAI Application Package 并可用 App Runner 本地调试

## 适用场景

- 开发医疗影像分割或分类推理应用并打包部署
- 将 DICOM 数据接入 MONAI 模型推理流水线
- 在本地调试后打包成可移植的推理应用包

## 场景标签

`图像视频处理` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L8: MONAI Deploy App SDK offers a framework and associated tools to design, develop and verify AI-driven applications in
> L15: - Out-of-the-box support for in-proc PyTorch based inference, as well as remote inference via Triton Inference Serv

## 星数曲线

```mermaid
xychart-beta
    title "Project-MONAI/monai-deploy-app-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 142 --> 144
    line [143, 143]
```

2026-10-18 143 → 2026-10-22 143（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `00e2df66b4d4` · [字段定义](../../DATASET.md)*
