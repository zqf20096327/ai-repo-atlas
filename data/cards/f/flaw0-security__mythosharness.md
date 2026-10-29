# flaw0-security/mythosharness

⭐ 18 · TypeScript · 推送 2026-05-25 · [GitHub](https://github.com/flaw0-security/mythosharness) · 个人维护

**让任意强编码模型执行长期自主漏洞挖掘的自进化 harness**

围绕任意强编码模型（Opus 4.7、GPT-5.5、DeepSeek V4、Gemini 等）构建的漏洞发现 harness，实现 Recon→Hunt→Validate→Gapfill→Report 流水线，由多个窄域并行 agent 组成。操作者通过邮件下达指令，harness 定期回邮件报告确认的漏洞；已确认的利用会被蒸馏为可自动加载的 markdown 技能，且 harness 可对自身源码提出补丁并经冒烟测试后提交。代码基于 @anthropic-ai/sdk 编写，非 Anthropic 模型需经 Thomas 路由。以 Bun 运行，PoC 在沙箱内执行并有 argv 白名单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Recon→Hunt→Validate→Gapfill→Report 多并行窄域 agent 流水线
- 邮件驱动 I/O：邮件下指令，定期回报告确认漏洞
- 技能蒸馏：确认的利用自动写入 markdown 技能供后续加载
- 自我变异：对自身源码提补丁，冒烟测试通过后才提交

## 适用场景

- 长时间无人值守地扫描仓库寻找可链式利用的漏洞
- 让安全研究员通过邮件远程下达目标与关注点
- 积累漏洞挖掘技能库以改进后续挖掘效果

## 场景标签

`Agent 框架` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L9: the right Recon → Hunt → Validate → Gapfill → Report pipeline around any
> L42: The fix is a structured pipeline of narrow, parallel agents with adversarial

## 星数曲线

```mermaid
xychart-beta
    title "flaw0-security/mythosharness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `123300e79fa2` · [字段定义](../../DATASET.md)*
