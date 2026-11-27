# wickedOne/infection-mate-extension

⭐ 3 · PHP · MIT · 推送 2026-11-23 · [GitHub](https://github.com/wickedOne/infection-mate-extension) · 个人维护

**让编码 agent 运行 Infection 变异测试并分析结果的 Symfony Mate 扩展**

Symfony Mate 的扩展插件，将 Infection 变异测试暴露为 agent 可调用的工具：运行 Infection（读取其 JSON 日志）、汇总 MSI 指标、按文件/变异器分页列出逃逸变异体并给出消灭提示，附工作流技能文件。基于 Composer 安装，依赖 infection/infection、测试框架与覆盖率驱动（pcov 或 xdebug）；缓存最近 10 次运行，来自被检项目的输出置于 untrusted_data 信封中返回。等价变异体甄别由 agent 完成，不自动抑制。

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

- infection-run/summary/escaped 三个工具加一个配置资源，供编码 agent 调用
- 读取 Infection 自身 JSON 日志，不修改用户配置，临时日志每次运行后删除
- 附 mate-infection-mutation-testing 技能，含工作流与等价变异体规则
- 可选安装 helgesverre/toon 以更省 token 的 TOON 格式编码响应

## 适用场景

- 让编码 agent 运行变异测试并自动补写能杀死逃逸变异体的测试
- 按文件或变异器排查逃逸变异体并理解其逃逸原因
- 在 CI 之外用 agent 对特定变异体 id 做局部重跑

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L10: A Symfony Mate extension that lets coding agents run Infection mutation testing and work with its results: find esc
> L32: Agents call them through the `vendor/bin/mate` CLI:

## 星数曲线

```mermaid
xychart-beta
    title "wickedOne/infection-mate-extension 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-30 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `c2248e6e6faa` · [字段定义](../../DATASET.md)*
