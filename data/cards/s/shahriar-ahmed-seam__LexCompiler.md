# shahriar-ahmed-seam/LexCompiler

⭐ 3 · TypeScript · MIT · 推送 2026-11-10 · [GitHub](https://github.com/shahriar-ahmed-seam/LexCompiler) · [官网](https://paragraph-rough-nickel-license.trycloudflare.com) · 个人维护

**给企业工程与法务团队：将法规文本编译为可验证的代码合规检查**

LexCompiler 读取法规源（GDPR、HIPAA、EU AI Act、EUR-Lex 等）与企业合同，将条款编译为道义逻辑谓词并生成 SMT-LIB2 断言与 OPA Rego 规则，对仓库的 AST 与 SQL DDL 用 Microsoft Z3 求解证明合规或违规（SAT/UNSAT）。检出违规时定位到具体 AST 节点与行号，经 CEGIS 合成代码补丁，附 Ed25519 签名证书与 SARIF 报告。以 MCP 服务器套件、Web 应用与 GitHub App 形式提供；RAG 检索依赖 Ollama 本地嵌入模型（可选），Z3 无法判定的规则标记为 action_required 而非通过。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个 MCP 服务器，支持 stdio/SSE/Streamable HTTP 三种传输
- Z3 定理证明合规判定，输出 Unsat Core 与反例模型
- Contextual + Graph RAG：384 维嵌入 + BM25 RRF 融合与知识图谱遍历
- GitHub App 以 check run 形式在 PR 上标注违规行

## 适用场景

- 对代码仓库自动核查数据保留、加密等法规条款
- PR 合并前以合规门禁拦截引入违规的提交
- 将法律团队批准的规则以 SARIF 报告交付安全审计

## 场景标签

`知识图谱` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L13: **LexCompiler** eliminates the manual translation layer between statutory text and source code. It ingests live reg
> L18: 3. Synthesizes an AST-preserving code patch via Counterexample-Guided Inductive Synthesis (CEGIS), verifies in an i
> L47: ### 1. Model Context Protocol (MCP) Server Suite (`server/mcp/`)

## 星数曲线

```mermaid
xychart-beta
    title "shahriar-ahmed-seam/LexCompiler 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 low · 依据 README sha `72096b2e6b69` · [字段定义](../../DATASET.md)*
