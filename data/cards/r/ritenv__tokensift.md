# ritenv/tokensift

⭐ 18 · TypeScript · MIT · 推送 2026-10-14 · [GitHub](https://github.com/ritenv/tokensift) · 个人维护

**面向 LLM prompt 的 token 效率静态检查工具**

以 TypeScript/npm 库与 CLI 双形态提供的 token 成本分析器：用供应商实际编码器对 prompt 字符串、Message[] 与工具 schema 做 tokenizer 级静态分析，20 条内置规则（uuid-bloat、pretty-json、repeated-block 等）定位浪费 token 的文本并给出实际美元成本；OpenAI 计数为精确值，Claude 无公开 tokenizer 故为校准估计并标注 confidence。支持 vitest/jest 匹配器、CI 集成（GitHub/SARIF 格式）、基线回归与部分安全 autofix，另可在 Deno/Workers 等边缘环境运行。自声明早期活跃开发状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 20 条内置规则检测 UUID、重复块、格式化 JSON 等 token 浪费并计算实际美元成本
- OpenAI 用真实 BPE 词表精确计数，Claude 为校准估计且逐条标注 confidence
- 提供 vitest/jest 测试匹配器与 CLI，输出 json/github/markdown/sarif 多种格式
- 支持 dyn() 模板槽区分静态/动态 token 与缓存破坏检测

## 适用场景

- 在 CI 或 pre-commit 中检查 prompt 文件的 token 成本回归
- 在测试套件里断言 prompt 不超过 token 预算
- 审计上线 prompt 中可削减的 token 浪费以降低调用费用

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: Token-efficiency linter for LLM prompts and payloads.
> L10: Deterministic, local, tokenizer-level static analysis of prompt strings, `Message[]` arrays, and tool schemas.
> L24: Two ways to use it: as a library, called from your own code or test suite, or as a CLI, pointed at prompt files and

## 星数曲线

```mermaid
xychart-beta
    title "ritenv/tokensift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e973d2ce7bbc` · [字段定义](../../DATASET.md)*
