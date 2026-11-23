# fuzzingbrain/FuzzingBrain-Bench

⭐ 10 · Python · MIT · 推送 2026-11-02 · [GitHub](https://github.com/fuzzingbrain/FuzzingBrain-Bench) · [官网](https://fuzzingbrain.github.io/benchmark.html) · 组织维护

**评测 LLM agent 发现与复现真实 0-day 漏洞的基准**

覆盖 43 个开源项目（C/C++/Java）77 个真实 0-day 漏洞的基准：agent 只拿到 fuzz harness 与漏洞版本源码，需在 sanitizer 下找到触发故障的输入。评分确定性（非 LLM-as-judge），在容器镜像内离线完成，按 distinct crash 加难度系数 D（1-5）计分，崩溃需 3 次复现且位置一致。通过 fb-bench CLI 驱动 API 模型或 Codex/Claude Code CLI 后端，也支持免 LLM 对外部 PoC 评分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 77 个 blind 挑战，答案密钥不随镜像分发
- 确定性评分：distinct crash × 难度系数，崩溃需 3 次复现
- 三种 agent 后端（api/codex/claudecode）共用同一入口
- 支持经 OpenAI 兼容端点接入自托管开源权重模型

## 适用场景

- 评测不同 LLM 在盲漏洞发现任务上的表现
- 用确定性判分对比多个模型的崩溃发现能力
- 对 AFL++/libFuzzer/honggfuzz 生成的 PoC 做统一验证

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3: **A benchmark for LLM-driven vulnerability reproduction on 77 real zero-day
> L9: sanitizer. Every grade is **deterministic** (no LLM-as-judge) and happens
> L17: |**77** end-to-end|**43**|C · C++ · Java|deterministic — in-image, offline|

## 星数曲线

```mermaid
xychart-beta
    title "fuzzingbrain/FuzzingBrain-Bench 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-18 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `22b5cde52e53` · [字段定义](../../DATASET.md)*
