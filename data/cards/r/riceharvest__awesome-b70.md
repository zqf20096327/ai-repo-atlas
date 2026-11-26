# riceharvest/awesome-b70

⭐ 4 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/riceharvest/awesome-b70) · [官网](https://riceharvest.github.io/awesome-b70/) · 个人维护

**Intel Arc Pro B70 本地跑 LLM 的设置指南与踩坑清单**

面向刚拿到 Intel Arc Pro B70 显卡、想在 Linux 上运行本地 LLM 的用户：收录环境自检脚本 b70-doctor、推理引擎选择表（Ollama/LM Studio/llama.cpp SYCL 与 Vulkan/vLLM XPU 等）、驱动与引擎已知问题的规避方案（带实时状态徽章）、SYCL 与 Vulkan 后端的实测基准数据、已测试模型清单。大部分内容也适用于 B60/B50/B580/B570。内容形式为清单与指南，本仓库不含模型实现或应用代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- b70-doctor 只读自检脚本：检查 xe 驱动、固件、Resizerable BAR、权限等并打印修复方法
- 引擎选择对比表覆盖 Ollama、llama.cpp SYCL/Vulkan、vLLM XPU、OpenVINO 等
- 已知驱动/引擎 bug 及规避方案，状态徽章实时更新
- 同机实测的 SYCL vs Vulkan、Mesa 25 vs 26 与 MTP 投机解码基准数据

## 适用场景

- 在 B70 上从零搭建本地 LLM 运行环境
- 选型合适的推理引擎和后端
- 遇到 GPU hang 或驱动重置时查找规避方案
- 参考实测数据决定 Mesa 版本与构建参数

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: Everything a new **Intel Arc Pro B70** (32 GB, Battlemage G31, `8086:e223`) owner needs to run local LLMs on Linux,
> L10: **Contents:** Start here · Pick an engine ·
> L16: 1. **Check the setup.** Run b70-doctor, a read-only script. It checks that

## 星数曲线

```mermaid
xychart-beta
    title "riceharvest/awesome-b70 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-21", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-26 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `e592ec65de75` · [字段定义](../../DATASET.md)*
