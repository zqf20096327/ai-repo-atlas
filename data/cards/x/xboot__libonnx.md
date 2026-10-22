# xboot/libonnx

⭐ 655 · C · MIT · 推送 2026-07-07 · [GitHub](https://github.com/xboot/libonnx) · 组织维护 · 中文 README

**面向嵌入式设备的纯 C99 ONNX 推理引擎库**

用纯 C99 实现的轻量级 ONNX 推理引擎，面向嵌入式设备与裸机环境，支持通过 resolver 数组接入硬件加速。.c/.h 文件可直接放入项目编译，也可用 make 构建静态库及示例（mnist 手写数字预测）与测试。基于 ONNX v1.17.0、支持 opset 24，部分算子尚未实现；支持 arm64 交叉编译，可用 xxd 将模型转为 C 数组直接嵌入。MIT 许可。

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

- 纯 C99 实现，源文件可直接嵌入项目编译
- 支持通过 resolver 传入硬件加速后端
- 基于 ONNX v1.17.0，支持 opset 24
- 提供 arm64 交叉编译与模型转 C 数组嵌入（xxd）方式

## 适用场景

- 在嵌入式或裸机设备上运行 ONNX 模型推理
- 将模型以字节数组形式编译进固件
- 通过自定义 resolver 接入硬件加速执行推理

## 场景标签

 · 领域:嵌入式机器学习推理

## 证据(README 行号)

> L2: A lightweight, portable pure `C99` `onnx` `inference engine` for embedded devices with hardware acceleration support
> L5: The library's .c and .h files can be dropped into a project and compiled along with it. Before use, should be alloca

## 星数曲线

```mermaid
xychart-beta
    title "xboot/libonnx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 654 --> 656
    line [655, 655]
```

2026-10-18 655 → 2026-10-22 655（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1aeba70a68a9` · [字段定义](../../DATASET.md)*
