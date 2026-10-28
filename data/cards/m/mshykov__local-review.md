# mshykov/local-review

⭐ 19 · Go · MIT · 推送 2026-09-30 · [GitHub](https://github.com/mshykov/local-review) · [官网](https://local-review.shykov.dev) · 个人维护

**本地 BYOK 多 LLM 代码审查 CLI：读 git diff 出审查报告**

Go 单二进制 CLI，读取 git diff，将 diff 分发给用户已认证的多个 LLM（Claude/Codex/Copilot CLI 并行编排，或 OpenAI 兼容端点如 Ollama/vLLM），合并各模型发现输出一份报告；major/critical 时以非零退出码接入 pre-commit 钩子。BYOK 模式密钥直连厂商，无 SaaS、无遥测，可用 Ollama 实现全离线。附带 OWASP 对齐的 CHECKLIST.md、10 例标注基准排行榜 bench/RESULTS.md 与全库审计命令。限制：diff 仍会发送到所配置的 LLM，Gemini 支持已标记停止服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 LLM 并行编排（Claude/Codex/Copilot CLI）并合并为单一报告
- OpenAI 兼容端点接入：Ollama/vLLM/DeepSeek 等，可全离线运行
- major/critical 非零退出码，可直接接入 pre-commit 钩子
- 仓库内置标注基准排行榜（bench/RESULTS.md）与 SLSA 签名的发布产物

## 适用场景

- 提交前在本地跑多模型代码审查，拦截 major/critical 问题
- 团队用 .local-review.yml 定制审查规则与严重度门槛
- 用局域网 Ollama 端点做不外发代码的离线审查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L6:  Runs against a git diff, hands it to whichever LLM you point it at, prints findings.
> L34: |An orchestrator that runs Claude / Gemini / Codex / Copilot CLIs in parallel and merges findings into one report|"
> L97: **Want a local-only or hybrid setup?** Add a provider entry under `llms.<name>:` with a `base_url:` pointing at any

## 星数曲线

```mermaid
xychart-beta
    title "mshykov/local-review 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `2138d1001970` · [字段定义](../../DATASET.md)*
