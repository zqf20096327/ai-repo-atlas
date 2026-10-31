# diohabara/pychd

⭐ 56 · Python · MIT · 推送 2026-05-27 · [GitHub](https://github.com/diohabara/pychd) · 个人维护

**Python .pyc 反编译器（3.0–3.14），规则层+LLM 混合并量化记忆污染**

读取 CPython 3.0–3.14 字节码并还原 .py 源码的反编译工具：确定性规则层恢复导入、声明、签名、装饰器、PEP 695/749 注解；默认 --hybrid-rewrite 模式再对每个模块调用一次 Codex CLI（gpt-5.5，复用 codex login 会话）补齐函数体，--rules-only 可离线无 LLM 运行。仓库另含两个独立 PyPI 包：pychd-pyfuzz 生成 LLM 未见的随机 Python，pychd-pyobf 匿名化 .pyc，用于量化基准中 LLM 记忆份额（2,794 模块、13 个语料库）。README 含大段数据污染披露，与 uncompyle6/decompyle3/pycdc/PyLingual 做了 23 模块对比。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性规则层离线可复现，支持 CPython 3.0–3.14 字节码
- 默认混合模式：每模块一次 Codex 调用补齐规则层无法恢复的函数体
- pychd-pyfuzz/pychd-pyobf 独立 PyPI 包，可对任意 Python 反编译器复用同一污染审计流水线
- raw 与 -obf 语料的差值用于量化 LLM 记忆份额（最多 −13.3 pt strict_match）

## 适用场景

- 从 .pyc 文件恢复 Python 源码（含最新 3.13/3.14 字节码）
- 安全审计场景下用 --rules-only 获得无 LLM 的确定性反编译
- 其他反编译器作者复用 fuzz→obfuscate→decompile 装置评估自身记忆污染
- 研究 LLM 辅助反编译基准中的训练数据污染问题

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: A Python `.pyc` decompiler that reads CPython 3.0 – 3.14 bytecode and
> L85: If you want a fully offline, deterministic, audit-friendly run with
> L86: no LLM calls and no contamination risk, use `--rules-only` — that is

## 星数曲线

```mermaid
xychart-beta
    title "diohabara/pychd 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-31 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `67ab1e34dd63` · [字段定义](../../DATASET.md)*
