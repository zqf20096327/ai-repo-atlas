# ait-aecid/rootkit-detection-ebpf-time-trace

⭐ 32 · Python · GPL-3.0 · 推送 2026-08-21 · [GitHub](https://github.com/ait-aecid/rootkit-detection-ebpf-time-trace) · 组织维护

**通过内核函数执行时间偏移检测 rootkit 文件隐藏的半监督工具**

由 AIT 维护的安全研究工具：用 eBPF 探针采集 getdents 系统调用链（含 filldir）多个内核函数的执行时间，配合开源 rootkit CARAXES 生成带/不带隐藏操纵的测量数据，再用基于统计检验的简单机器学习模型做半监督异常检测，输出检测指标与混淆矩阵。提供公开 Zenodo 数据集，检测部分只需 Python 依赖即可独立运行。探测与 rootkit 部分依赖 CARAXES 仓库并需替换 hooks.h 后编译，在 Linux 内核 5.15-6.11、Python 3.10 上测试过。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- eBPF 探针采集 getdents 调用链内核函数执行时间
- 半监督统计检验模型检测时间偏移，输出指标与混淆矩阵
- 依赖 CARAXES rootkit 生成对照数据，公开 Zenodo 数据集
- 检测模块可脱离采集部分独立运行

## 适用场景

- 研究 rootkit 文件隐藏行为在内核时序上的痕迹
- 复现论文数据采集与异常检测评估流程
- 基于公开数据集实验半监督时序异常检测方法

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains code to collect time measurements of kernel functions that are manipulated by rootkits when
> L6: * Landauer, M., Alton, L., Lindorfer, M., Skopik, F., Wurzenberger, M., & Hotwagner, W. (2025). Trace of the Times: 

## 星数曲线

```mermaid
xychart-beta
    title "ait-aecid/rootkit-detection-ebpf-time-trace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `75b9db295d56` · [字段定义](../../DATASET.md)*
