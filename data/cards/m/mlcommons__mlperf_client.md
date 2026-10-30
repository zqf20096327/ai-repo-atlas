# mlcommons/mlperf_client

⭐ 95 · C++ · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/mlcommons/mlperf_client) · [官网](https://mlcommons.org/benchmarks/client/) · 组织维护

**面向个人设备的 ML 推理性能基准测试工具（命令行）**

MLCommons 的 MLPerf Client 基准：在 Windows/macOS 个人电脑上测量 LLM 聊天、图像分类等 ML 推理场景的性能，通过 JSON 配置文件指定硬件与推理参数，以单个二进制文件分发，模型与数据文件按需下载。支持各独立硬件厂商以 Execution Provider 形式接入自有模型格式与推理栈，可枚举设备、导出 CSV 结果、校验数据文件 SHA256。iOS 版仅提供 GUI，不支持 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 AI 聊天（Llama 2 等）与图像分类等客户端推理场景
- IHV 以 Execution Provider 形式提供各自模型格式与推理栈路径
- JSON 配置文件定义场景、模型、迭代次数与执行提供方
- 结果可导出 CSV，数据文件支持 SHA256 完整性校验

## 适用场景

- 测量本机在不同硬件/软件配置下的推理性能
- 硬件厂商为自己的推理栈接入并参与客户端基准测试
- 按设备枚举批量跑基准并汇总 CSV 结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: MLPerf Client is a benchmark for Windows and macOS, focusing on client form factors in ML inference scenarios like A
> L11: The MLPerf Client benchmark measures the performance of inference tasks on personal computers. It supports the foll

## 星数曲线

```mermaid
xychart-beta
    title "mlcommons/mlperf_client 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 93 --> 96
    line [94, 95, 95]
```

2026-10-18 94 → 2026-10-30 95（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1afd5171fc27` · [字段定义](../../DATASET.md)*
