# whystrohm/digital-twin-of-yourself

⭐ 23 · Python · MIT · 推送 2026-11-14 · [GitHub](https://github.com/whystrohm/digital-twin-of-yourself) · [官网](https://whystrohm.com) · 个人维护

**从你的写作提取可测试的个人数字分身 System Prompt 工具**

以个人写作语料为输入，生成三层工作流：脚本测量句长、对冲率、重复短语等模式并输出 HTML 报告；结合 LLM 提取与至多五个补充问答，生成捕捉个人文风与决策方式的 System Prompt（Twin）；twin_check.py 按规则逐行检查草稿并以退出码接入 CI 门控，twin_diff.py 从草稿与实际发送稿的配对中提出规则变更供人工勾选采纳。分层适配任意 LLM、Claude 记忆模式与 Claude Code。脚本为标准库 Python，离线运行，读取时自动脱敏邮箱/电话/金额。面向希望审计与统一文风的个人与团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- twin_scan.py 测量句长/对冲率/重复短语/文件漂移等模式，输出 HTML 报告
- 生成个人文风 System Prompt 与可机检的 twin.rules.json
- twin_check.py 逐行检查草稿，退出码可门控 CI，GitHub diff 格式标注
- 15 项对抗压力测试与 10 维评分表验证 Twin

## 适用场景

- 从我的写作语料生成代表我文风的 System Prompt
- 在 pull request 中自动拦截偏离我的文风的文案
- 对比多个品牌/语气的分身并按提案流程更新规则

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L14: |**A twin any AI can use**|A System Prompt that captures your voice and how you decide, built from your writing plu
> L47: |**1**|Any LLM (ChatGPT, Gemini, Claude)|Writing you paste in|The model estimates|
> L63: 3. It runs `twin_scan.py`, reads the numbers instead of guessing them, interviews you about the gaps (at most five 

## 星数曲线

```mermaid
xychart-beta
    title "whystrohm/digital-twin-of-yourself 星数(近 2 点)"
    x-axis ["2026-11-14", "2026-11-21"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-11-14 23 → 2026-11-21 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `632b71d31e5e` · [字段定义](../../DATASET.md)*
