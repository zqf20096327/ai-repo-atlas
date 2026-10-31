# luxonis/modelconverter

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/luxonis/modelconverter) · [官网](https://www.luxonis.com/) · 组织维护

**将 ONNX/OpenVINO/TFLite 模型转换为 Luxonis 相机可用格式**

面向 Luxonis 相机（OAK 系列，RVC2/RVC3/RVC4/Hailo 平台）用户的模型编译工具：读取 ONNX、OpenVINO IR、TensorFlow Lite 模型及 NN Archive，转换为可在相机上运行的格式。通过 PyPI 安装的 CLI 使用，支持云端（HubAI SDK）与本地两种转换方式；本地模式依赖 Docker，官方提供各平台预构建镜像，也支持自行构建并配置 OpenVINO、SNPE、Hailo 等转换工具包。处于实验性公开测试阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 ONNX/OpenVINO IR/TensorFlow Lite 输入格式
- 覆盖 RVC2/RVC3/RVC4/Hailo 四类平台，官方 Docker 预构建镜像
- NN Archive 与 YAML 两种配置方式，CLI 参数可覆盖设置
- 支持云端（HubAI SDK）与本地（Docker）转换

## 适用场景

- 把训练好的 ONNX 模型部署到 Luxonis OAK 相机
- 在本地 Docker 环境中离线转换模型，不将模型上传云端
- 配置色彩编码与预处理参数以匹配模型输入要求

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L12: Convert your **ONNX**, **OpenVINO IR** and **TensorFlow Lite** models to a format compatible with any generation of
> L23: The easiest way to use ModelConverter is to use the `modelconverter` CLI.
> L133: We provide official Docker images for `RVC2`, `RVC3` and `RVC4` platforms.

## 星数曲线

```mermaid
xychart-beta
    title "luxonis/modelconverter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `6d8e2587dd29` · [字段定义](../../DATASET.md)*
