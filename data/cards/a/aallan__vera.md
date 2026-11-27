# aallan/vera

⭐ 424 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/aallan/vera) · [官网](https://veralang.dev/) · 个人维护

**为 LLM 编写而设计的编程语言：契约强制、编译到 WebAssembly**

Vera 是一门面向大语言模型作者的编程语言，名字取自拉丁语 veritas。语言层面取消变量名（用 @Int.0 等结构化引用）、强制契约（requires/ensures 由 Z3 静态证明或转为运行时检查）、效果类型化（LLM 调用、HTTP 须在签名声明），诊断信息按'给模型看的修复指令'格式输出并支持 JSON。程序编译为 WebAssembly，可在命令行、浏览器或 WASI 0.2 主机运行。通过 PyPI 发行 veralang，提供 vera check/verify/errors 命令与语言服务器（lsp 扩展）。不支持 macOS 14 及更早版本与低版本 glibc 的 Linux aarch64。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 契约强制：requires/ensures 由 SMT 求解器静态证明或降级为运行时检查
- 变量名被结构化引用取代，效果在函数签名中显式声明（如 <Inference>、<Http>）
- SQL 注入形态（字符串拼接查询）在类型检查阶段无法编译（E207）
- 错误诊断含错误原因、修复示例与规范引用，支持 --json 结构化输出

## 适用场景

- 让 LLM agent 编写带强制契约的 Vera 代码并由 vera verify 校验
- 将可验证的程序编译为 WebAssembly 在命令行或浏览器运行
- 从语言层面消除 SQL 注入等字符串拼接类漏洞
- 研究面向 AI 代码生成的语言设计与形式化验证结合

## 场景标签

 · 领域:编程语言/程序验证

## 证据(README 行号)

> L10: **Vera** (v-ERR-a) is a programming language designed for large language models to write. The name comes from the L
> L158: The workflow: an LLM agent writes Vera with mandatory contracts; vera check and vera verify check every type and p

## 星数曲线

```mermaid
xychart-beta
    title "aallan/vera 星数(近 9 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-16", "2026-11-20", "2026-11-27"]
    y-axis "stars" 417 --> 425
    line [418, 419, 420, 418, 420, 421, 423, 424, 424]
```

2026-10-25 418 → 2026-11-27 424（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `e6b744e47b7e` · [字段定义](../../DATASET.md)*
