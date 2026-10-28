# andykear/FileMaker-XMLsnippet-Claude-Skill

⭐ 19 · CC-BY-4.0 · 推送 2026-10-03 · [GitHub](https://github.com/andykear/FileMaker-XMLsnippet-Claude-Skill) · [官网](https://clockworkct.co.uk) · 组织维护

**FileMaker 脚本 XML 粘贴规范的逆向文档与 Claude 技能包**

对 FileMaker 未公开的 fmxmlsnippet 剪贴板格式做逆向工程的经验性规范：覆盖 FileMaker 2026 全部 222 个脚本步骤 ID、每个步骤的规范 XML 骨架、元素排序约束与计算槽绑定规则，文档化粘贴时的静默失败模式（如变量名丢失、计算槽错绑）。以 Claude skill 形式打包，采用渐进加载（按任务读取所需步骤类别以控制 token 用量），参考文件为纯 markdown，可被任意 LLM 或人工读取。安装方式为下载 Releases 的 zip 并上传至 Claude 组织技能库；粘贴测试基于 MBS Plugin，许可为 CC BY 4.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 FileMaker 2026 全部 222 个脚本步骤 ID 的经验验证字典
- 文档化三类静默失败：变量名丢失、计算槽错绑、元素排序
- 渐进加载的 Claude skill 打包，按需读取降低 token 消耗
- 规范文件为纯 markdown，模型无关，可供其他工具集成

## 适用场景

- 让 Claude 生成可正确粘贴进 FileMaker 的脚本 XML
- 审查已有 fmxmlsnippet XML 中的粘贴处理器错误
- 构建自动生成 FileMaker 脚本 XML 的工具时复用该规范

## 场景标签

`代码生成` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L6: Reverse-engineered specification of FileMaker's undocumented `fmxmlsnippet` clipboard format. Every step ID, element
> L28: ## Packaged as a Claude Skill
> L38: The specification is packaged here as a Claude skill, but the format rules are model-agnostic. The reference files 

## 星数曲线

```mermaid
xychart-beta
    title "andykear/FileMaker-XMLsnippet-Claude-Skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2c84fbeefffe` · [字段定义](../../DATASET.md)*
