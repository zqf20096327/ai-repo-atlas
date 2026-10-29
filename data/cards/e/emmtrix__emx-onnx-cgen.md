# emmtrix/emx-onnx-cgen

⭐ 40 · Python · Apache-2.0 · 推送 2026-07-29 · [GitHub](https://github.com/emmtrix/emx-onnx-cgen) · [官网](https://www.emmtrix.com/wiki/emmtrix_ONNX-to-C_Code_Generator) · 组织维护

**把 ONNX 模型编译为可审计 C 代码的嵌入式 AI 编译器**

面向深度嵌入式与安全关键系统的 ONNX-to-C 编译器（PyPI 包 + CLI）：读取 ONNX 模型，经 import→normalize→optimize→lower→emit 流程生成静态、确定性的 C 代码，支持完整 ONNX opset 26 与 >99% 算子覆盖率，数据类型覆盖 float16/8bit/4bit/整型等。生成代码可无 OS 依赖运行，可选完全免动态分配（权重嵌入源码或外置 .bin 加载），并与 ONNX Runtime 做端到端验证比对。限制：不做激进性能优化（交由 emmtrix Edge AI Compiler）、不支持训练和需动态 shape 的模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 ONNX opset 26（基于 ONNX 1.21.0），算子覆盖率 >99%
- 静态编译期内存布局，可选完全免 malloc/free 分配
- 生成代码无 OS 依赖、单线程、逐位稳定的可复现代码生成
- CLI compile/verify 子命令 + 可作为导入式 ONNX backend

## 适用场景

- 把 ONNX 模型编进裸机/RTOS 固件，权重以 static const 存于 flash
- 资源受限且需认证审计的安全关键固件中运行模型
- 用 ONNX Runtime 比对验证生成 C 代码的输出正确性
- 作为 emmtrix Edge AI Compiler 的正确性优先前端

## 场景标签

 · 领域:嵌入式/边缘 AI 工具链

## 证据(README 行号)

> L7: **emmtrix ONNX-to-C Code Generator (emx-onnx-cgen)** compiles ONNX models to portable, deterministic C code for deep
> L38: - Clean, pass-based compiler architecture (import → normalize → optimize → lower → emit).
> L50: - CLI for ONNX-to-C compilation and verification.

## 星数曲线

```mermaid
xychart-beta
    title "emmtrix/emx-onnx-cgen 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-29 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `659ac4bbae43` · [字段定义](../../DATASET.md)*
