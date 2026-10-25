# VeriSilicon/tflite-vx-delegate

⭐ 48 · C++ · MIT · 推送 2026-03-12 · [GitHub](https://github.com/VeriSilicon/tflite-vx-delegate) · 组织维护

**面向 VeriSilicon NPU 的 TensorFlow Lite 外部 delegate**

基于 TIM-VX（OpenVX）实现的 TensorFlow Lite 外部 delegate 库，使 TFLite 模型能在 VeriSilicon/Vivante NPU（含 VIPLite 驱动）上运行。通过 CMake 从源码构建，非交叉构建时自动下载 tim-vx 与 tensorflow（会对 tensorflow 树打补丁以启用外部 delegate 与 NBG 支持），交叉构建需先构建 tim-vx 并指定 Vivante SDK。附带 benchmark_model/label_image 示例、Python label_image 示例、单元测试与 NPU/CPU 结果对比脚本，支持 Acuity Toolkit 生成的 NBG 自定义算子格式与缓存模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 TIM-VX 将 TFLite 算子映射到 VeriSilicon NPU 执行
- 支持 VIPLite 驱动（要求 Vivante SDK >= 6.4.22、ovxlib >= 1.2.26、viplite >= 2.0.0）
- 支持 Acuity Toolkit 生成的 NBG 编译图作为自定义算子
- 提供 NPU 与 CPU 结果对比的模型验证脚本与缓存模式

## 适用场景

- 在 VeriSilicon/Vivante NPU 硬件上部署 TFLite 模型
- 用 benchmark_model/label_image 在 NPU 上跑推理与性能测试
- 对比 NPU 与 CPU 推理结果做模型验证

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: # TfLite-vx-delegate
> L2: TfLite-vx-delegate constructed with TIM-VX as an openvx delegate for tensorflow lite. Before vx-delegate, you may ha

## 星数曲线

```mermaid
xychart-beta
    title "VeriSilicon/tflite-vx-delegate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-25 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ad4edd4d88be` · [字段定义](../../DATASET.md)*
