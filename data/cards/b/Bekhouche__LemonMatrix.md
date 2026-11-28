# Bekhouche/LemonMatrix

⭐ 8 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/Bekhouche/LemonMatrix) · [官网](https://lemonmatrix.github.io) · 个人维护

**为 Lemonade 本地 AI 服务器跑基准测试并提交可验证结果**

面向 Lemonade 实例的基准测试控制平面：自动发现并保存本机 Lemonade 实例为 profile，作为该机器每次运行的环境指纹；以固定提示词、禁用 prompt 缓存、检测驻留模型等方式判定结果有效性，防止缓存命中和内存占用造成的失真数据。支持 Ryzen AI NPU/Hybrid/CPU 引擎扫描、混合本地-云端路由的成本核算、omni 多模态任务端到端测量，并将结果以 PR 形式提交到公共排行榜，另提供本地 Flask 仪表盘。需 Python 3.10+。

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

- 环境指纹 profile 机制：一台机器一个实例，跨运行复用
- 有效性校验：禁用 prompt 缓存计时 TTFT/prefill，检测其他驻留模型并拒绝排名
- 路由成本运行：记录请求本地/云端分配与美元成本对比
- lemonmatrix import 读取 lemonade_lab、LemonMetrics 等外部结果并标记 validated: false

## 适用场景

- 把本机 Lemonade 的 LLM 性能测试结果提交到公共排行榜
- 在多台机器的局域网内批量发现实例并做 sweep 测试
- 评估本地硬件能接管多少云端路由流量与成本
- 对比 Ryzen AI NPU/Hybrid/CPU 不同部署方式的延迟

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A benchmarking control plane for Lemonade instances.
> L15: there, gated by CI running `lemonmatrix validate-submission` against the

## 星数曲线

```mermaid
xychart-beta
    title "Bekhouche/LemonMatrix 星数(近 3 点)"
    x-axis ["2026-11-13", "2026-11-14", "2026-11-28"]
    y-axis "stars" 6 --> 9
    line [7, 8, 8]
```

2026-11-13 7 → 2026-11-28 8（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `654319c203cd` · [字段定义](../../DATASET.md)*
