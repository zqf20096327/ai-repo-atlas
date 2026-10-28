# ParamThakkar123/simulusion

⭐ 31 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ParamThakkar123/simulusion) · [官网](https://paramthakkar123.github.io/simulusion/) · 个人维护

**统一 API 训练多种世界模型的 PyTorch 库**

模块化 PyTorch 库，将 Dreamer、PlaNet、IRIS、JEPA、DIAMOND、DiT、Genie 等世界模型算法纳入同一套 create_config / create_model / make_env 工厂接口，并提供统一的 Trainer 与 YAML 运行配置。支持 Gym/Gymnasium、MuJoCo、Brax、Unity ML-Agents 等环境适配，可从录制数据（含 LeRobot 机器人数据）训练世界模型，并导出 ONNX / TorchScript / TensorRT。面向强化学习研究者与开发者，通过 PyPI 安装，demo 可在笔记本 GPU（RTX 3050, 4 GB）上一至两小时跑通。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 十余种世界模型算法共享同一工厂 API 与统一 Trainer/YAML 配置
- 环境适配器覆盖 Gym/Gymnasium、MuJoCo、Brax、Unity ML-Agents 等
- 支持从录制数据（含 LeRobot 机器人数据）训练世界模型并对接自定义 agent
- ONNX / TorchScript / TensorRT 导出内建

## 适用场景

- 在统一接口下训练并对比 Dreamer、PlaNet、IRIS 等世界模型算法
- 从机器人或视频录制数据训练世界模型供规划使用
- 基于模块化编码器/解码器/动力学组件组合自定义架构

## 场景标签

`强化学习` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L14: **Simulusion brings the major world-model families together under a single PyTorch API.** Train Dreamer, PlaNet, JE
> L134: |Name|Algorithm|Description|Key Features|

## 星数曲线

```mermaid
xychart-beta
    title "ParamThakkar123/simulusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `dc55ca5520f1` · [字段定义](../../DATASET.md)*
