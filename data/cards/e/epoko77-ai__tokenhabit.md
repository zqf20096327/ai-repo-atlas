# epoko77-ai/tokenhabit

⭐ 19 · Python · MIT · 推送 2026-08-16 · [GitHub](https://github.com/epoko77-ai/tokenhabit) · [官网](https://pypi.org/project/tokenhabit/) · 个人维护 · 中文 README

**扫描 Claude Code 本地日志、定位浪费 token 的使用习惯的 CLI**

面向 Claude Code 用户的离线分析 CLI：读取 ~/.claude/projects 下的 JSONL 日志，检测 11 种可定量测量的 token 浪费习惯（上下文过载、文件重复读取、模型中途切换等），输出排名与对应 fix，并给出浪费分数（区分实测/换算/启发式/信号四类）。无 LLM 调用、无依赖，除 opt-in --ccusage 外不联网。另提供 Claude Code 技能包做 31 模式交互式辅导。通过 PyPI/uvx/pipx 安装。

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

- 离线扫描 ~/.claude 日格日志，检测 11 种 token 浪费习惯并给出 fix
- 无 LLM 调用、零依赖，除 opt-in --ccusage 外不联网
- 浪费分数区分 observed/estimated/heuristic/signal 四类口径
- 附带 Claude Code 技能包覆盖 31 模式的交互式辅导

## 适用场景

- 查看最近哪些使用习惯在消耗 Claude Code token
- 按报告建议调整 /compact、模型路由等操作降低浪费
- 配合 ccusage 同时查看用量与习惯诊断

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L16: LLM 호출 0회. 의존성 0개. 내 `~/.claude` 로그 위에서 오프라인으로 작동합니다 — 네트워크를 쓰는 건
> L49: 그다음 `tokenhabit --lang ko` 만 실행하면 됩니다. 최근 7일 `~/.claude/projects/**/*.jsonl` 을 스캔해 리포트를 출력합니다.
> L124: 모두 로컬에서 작동합니다. 내 `~/.claude` 로그 파일만 읽으며 어디로도 전송하지 않습니다. (opt-in `--ccusage` 플래그만 `npx ccusage` 를 호출하며, 이때 npm 레지스트

## 星数曲线

```mermaid
xychart-beta
    title "epoko77-ai/tokenhabit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3d29f9ecd589` · [字段定义](../../DATASET.md)*
