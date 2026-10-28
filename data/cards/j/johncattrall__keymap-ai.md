# johncattrall/keymap-ai

⭐ 24 · Python · MIT · 推送 2026-09-26 · [GitHub](https://github.com/johncattrall/keymap-ai) · 个人维护

**让编码 Agent 成为键盘固件专家的 Agent Skill**

面向 Claude Code、Codex CLI、Cursor、Gemini CLI、opencode 等 Agent Skills 标准框架的技能包：通过 SKILL.md 意图路由，让 Agent 审计 ZMK/QMK 键盘配置、调优 home row mods、使轨迹球分层感知、生成 keymap-drawer 图表、在 CI 中用 sync_keymaps.py 校验 ZMK 与 QMK 两块键盘布局漂移，并按 22 条实测坑库调试固件错误。支持 Colemak-DH、Graphite 等替代布局。ZMK/QMK 支持层级均为 Stable，QMK 指点设备配方暂缓。

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

- 审计 ZMK/QMK 配置并按收益排序输出发现与修复方案
- sync_keymaps.py CI 脚本以等价表保持 ZMK/QMK 双键盘布局同步
- keymap-drawer 生成分层键位图（支持暗色模式与轨迹球绘制）
- 22 条实测固件坑库与构建错误排查手册

## 适用场景

- 让 AI 助手审计并迭代我的 ZMK/QMK 键盘配置
- 两块键盘分别用 ZMK 和 QMK 时保持布局不漂移
- 自动生成每层键位图并入 CI

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: An Agent Skill that turns your coding agent into a custom-keyboard firmware expert. Audit your ZMK or QMK config, tu
> L10: Works with Claude Code, Codex CLI, Cursor, Gemini CLI, opencode, and any other harness supporting the Agent Skills 
> L95:   SKILL.md                  intent routing: audit / apply / pointing / draw / layout / platform / debug

## 星数曲线

```mermaid
xychart-beta
    title "johncattrall/keymap-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-28 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2607a6acb0dc` · [字段定义](../../DATASET.md)*
