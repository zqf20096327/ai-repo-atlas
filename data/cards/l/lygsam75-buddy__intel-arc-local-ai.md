# lygsam75-buddy/intel-arc-local-ai

⭐ 3 · Python · MIT · 推送 2026-11-09 · [GitHub](https://github.com/lygsam75-buddy/intel-arc-local-ai) · 个人维护 · 中文 README

**Intel Arc Pro B 系列显卡本地 AI 实测数据手册**

对四款 Intel Arc Pro 显卡（B50/B60/B65/B70）上 llama.cpp（SYCL）与 ComfyUI 的聊天、图像、视频、音乐生成进行实测，记录配置与每张卡的吞吐、时长、功耗数据，所有数字附原始日志与机器可读数据并标注证据状态。提供 6.0 GB 免配置整合包（含 torch、XPU 运行时与补丁）、纯聊天用的 llama.cpp zip 免 Python 路线，以及打包好的 ComfyUI 工作流与模型合集（百度网盘分发）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四张卡的聊天 tok/s、图像/视频/音乐生成时长、全载功耗均为实测并附原始日志
- 每条数据带 DEV+SUBSYS 板卡 ID 与证据状态，附测试注册表说明测了什么、没测什么
- 6.0 GB 免配置整合包：解压即用，聊天路线无需 Python
- 附带 intel-studio-pack：12 个工作流 + 13 个模型 + SOP

## 适用场景

- 为本地部署选一块合适的 Intel Arc Pro 显卡
- 查询某张卡跑 35B 聊天或 1080p 视频生成的实际速度和功耗
- 在 Intel 卡上跳过手动配 torch/XPU 环境直接生成图像

## 场景标签

`模型评测` `图像生成` `视频生成` · 领域:评测与运维

## 证据(README 行号)

> L12: **Only the configurations we actually ran, and the numbers we actually measured** — with raw logs,
> L18: > 🧾 **Distrust a number?** Every figure below traces to one file in `bench/data/`,
> L5: Field-measured local AI on Intel Arc Pro **B50 (16 GB)**, **B60 (24 GB)**, **B65 (32 GB)** and **B70 (32 GB)** —

## 星数曲线

```mermaid
xychart-beta
    title "lygsam75-buddy/intel-arc-local-ai 星数(近 2 点)"
    x-axis ["2026-11-12", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-12 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `89ff036acb3f` · [字段定义](../../DATASET.md)*
