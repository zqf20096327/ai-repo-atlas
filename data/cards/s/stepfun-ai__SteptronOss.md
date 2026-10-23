# stepfun-ai/SteptronOss

⭐ 589 · Python · Apache-2.0 · 推送 2026-09-04 · [GitHub](https://github.com/stepfun-ai/SteptronOss) · 组织维护 · 中文 README

**轻量级 LLM 训练框架：SFT/RLVR/评测的模块化实验**

阶跃星辰开源的大语言模型训练框架，覆盖 SFT、评测与（进行中的）RLVR 工作流。以配置驱动实验，提供 cfshow 动态查看与 sanity_check 校验，数据/优化器/模型栈可扩展；可仅以 PyTorch 为依赖运行，另支持 flash-attn、grouped_gemm 等算子级替换加速。分布式 rendezvous 通过共享目录自启每实验 Redis 服务；附多节点启动脚本生成工具与 AGENTS.md 供 AI agent 参与贡献。RLVR 实现尚未完成。

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

- 配置驱动实验，cfshow 查看与 sanity_check 动态校验
- 可仅以 PyTorch 为依赖运行，支持算子级替换加速（flash-attn/grouped_gemm）
- 多节点启动脚本生成工具与基于 Redis 的分布式 rendezvous
- 附 AGENTS.md 支持 AI agent 参与代码修改

## 适用场景

- 用 Qwen3 等参考配置跑 SFT/预训练实验
- 快速迭代与复现 LLM 训练实验
- 多机分布式训练的脚本生成与环境管理

## 场景标签

 · 领域:LLM 训练框架

## 证据(README 行号)

> L5: **StepTronOSS** is a lightweight **training framework** for large-scale language models with a focus on modular conf
> L144: - [x] SFT exps

## 星数曲线

```mermaid
xychart-beta
    title "stepfun-ai/SteptronOss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 588 --> 590
    line [589, 589]
```

2026-10-18 589 → 2026-10-23 589（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `d3e983d6ec8d` · [字段定义](../../DATASET.md)*
