# etinpres/mindvault

⭐ 15 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/etinpres/mindvault) · 个人维护

**给 Claude Code/Codex 的跨会话共享永久记忆系统**

面向 macOS Apple Silicon 用户的 Claude Code·Codex 共享记忆系统，解决每次会话上下文清零问题。5 层管道：SessionStart 自动注入近 5 会话摘要、/recall 自然语检索（SQLite FTS5+Arctic-ko 嵌入 RRF）、Memory Compiler（本地 Gemma 在会话结束提取可留存的决策/事实）、每次输入时的 hybrid 自动记忆回收、Gemma 4-way 矛盾检测。提取候选进入 staged 目录经 /memory_review 人工审批，防止静默错误记忆。生成用本地 Gemma、嵌入用本地 Arctic-ko，仅 L1 摘要调用 Claude Haiku 且传输前去除凭据模式。限制：仅支持 Apple Silicon Mac，Linux/Windows 不可用，launchd 与 MLX 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 层管道：会话摘要注入·自然语检索·Memory Compiler·自动回收·矛盾检测
- FTS5 + Arctic-ko 嵌入 hybrid 检索，Gemma 重排
- staged 记忆经 /memory_review 人工审批后进入永久记忆
- Claude Code 与 Codex 共享同一记忆库（含 agent 标签计测与幂等键提取）

## 适用场景

- 让 Claude Code 在新会话中自动找回过去项目的决策与配置
- 用自然语检索全部历史会话与记忆
- Codex 与 Claude Code 共享同一份永久记忆库

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: > Claude Code·Codex의 공유 영구 기억 시스템. 5-layer 파이프라인으로 세션 요약 자동 주입 · 자연어 검색 · Memory Compiler · 자동 회수 · 모순 감지까지 — 두 에이전트
> L25: 2. **메모리 회수** — UserPromptSubmit 마다 hybrid 검색으로 관련 메모리를 system-reminder에 자동 주입
> L26: 3. **자동 컴파일** — SessionEnd/Stop마다 로컬 Gemma가 새 대화 구간에서 영구로 남길 가치가 있는 결정/노하우/사실을 추출, 검토 후 영구 메모리에 진입

## 星数曲线

```mermaid
xychart-beta
    title "etinpres/mindvault 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ba4e103ccfa3` · [字段定义](../../DATASET.md)*
