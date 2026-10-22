# RealAlexandreAI/json-repair

⭐ 384 · Go · GPL-3.0 · 推送 2026-10-21 · [GitHub](https://github.com/RealAlexandreAI/json-repair) · [官网](https://pkg.go.dev/github.com/RealAlexandreAI/json-repair) · 个人维护 · 中文 README

**修复 LLM 输出的畸形 JSON 的 Go 库与 CLI**

json_repair 的 Go 移植，模块为 github.com/RealAlexandreAI/json-repair，Go 1.21，无第三方依赖。核心入口 RepairJSON/MustRepairJSON 返回紧凑合法 JSON，RepairWithOptions 提供解析值、修复日志、严格模式、流式稳定字符串与 JSON Schema 引导修复（standard/salvage 两模式）。normalize 阶段剥离代码围栏与注释、映射全角标点。以 Go 库形式提供，附 CLI（brew 或 Releases 二进制安装）。限制：输出键序不稳定，无 stdin 管道模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RepairWithOptions 支持 Schema 引导修复与 salvage 模式
- normalize 处理代码围栏、注释、全角标点映射
- 零第三方依赖的纯 Go 模块
- CLI 以 Homebrew 公式与三平台预编译二进制发布

## 适用场景

- 修复 LLM 输出中不完整或畸形的 JSON 再解析
- 在 Go 后端对模型流式输出做部分字符串修复
- 按 JSON Schema 校验并挽救模型生成的结构化数据

## 场景标签

 · 领域:LLM 工具链/数据处理

## 证据(README 行号)

> L5: Repair malformed JSON from LLM output into compact, valid JSON.
> L14: A Go library and a small CLI. The module is `github.com/RealAlexandreAI/json-repair`, Go 1.21, with no third-party 

## 星数曲线

```mermaid
xychart-beta
    title "RealAlexandreAI/json-repair 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 383 --> 385
    line [384, 384]
```

2026-10-18 384 → 2026-10-21 384（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0aff6753bff1` · [字段定义](../../DATASET.md)*
