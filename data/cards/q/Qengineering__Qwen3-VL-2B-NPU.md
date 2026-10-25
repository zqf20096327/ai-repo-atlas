# Qengineering/Qwen3-VL-2B-NPU

⭐ 42 · C++ · BSD-3-Clause · 推送 2026-07-22 · [GitHub](https://github.com/Qengineering/Qwen3-VL-2B-NPU) · [官网](https://qengineering.eu/deep-learning-examples-on-raspberry-32-64-os.html) · 个人维护

**在 RK3588 NPU 上运行 Qwen3-VL-2B 视觉语言模型的 C++ 应用**

Qengineering 提供的 C++ 应用，将 Qwen3-VL-2B 视觉语言模型部署到 Rockchip RK3588（Rock 5、Orange Pi 5）的 NPU 上：LLM 部分量化为 w8a8 走 RKLLM，视觉编码器以 fp16 走 RKNN。用户通过命令行输入图片与提问，模型生成图像描述并支持多轮对话（<image>/<clear>/<exit> 控制符）。需自行下载约 2.3 GB 的两个模型文件，依赖 OpenCV、rkllm-runtime 1.2.3 与 rknpu 驱动 0.9.8，附多模型 tokens/s 基准表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM（w8a8 量化）与视觉编码器（fp16）分别通过 RKLLM/RKNN 运行于 RK3588 NPU
- 命令行交互式图像问答，支持多轮对话记忆与 <image>/<clear>/<exit> 控制符
- 提供约 15 个 VLM 在 RK3588 上的内存占用与 tokens/s 基准表
- 仓库内置指定版本 rkllm/rknn 运行库及 CMake/Code::Blocks 两种构建方式

## 适用场景

- 在 Rock 5 / Orange Pi 5 等开发板上离线运行视觉问答
- 边缘设备上测试小型 VLM 的性能与内存占用
- 参考 C++ 代码学习 RKLLM/RKNN 多模态部署

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L18: ## Qwen3-2B VLM for RK3588 NPU (Rock 5, Orange Pi 5).
> L34: Once converted to RKNN, parts of the model can run on the NPU, improving speed.

## 星数曲线

```mermaid
xychart-beta
    title "Qengineering/Qwen3-VL-2B-NPU 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `21fc9d9bad2f` · [字段定义](../../DATASET.md)*
