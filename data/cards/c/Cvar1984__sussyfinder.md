# Cvar1984/sussyfinder

⭐ 77 · PHP · GPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/Cvar1984/sussyfinder) · 个人维护

**单文件 PHP webshell 扫描器：规则+统计+小型ML检测后门**

自包含的 PHP 单文件 Web 应用，递归扫描目录下的 PHP 文件，通过 token 模式匹配（eval/exec 等危险函数、拼接隐藏函数名、回调执行等结构信号）、MD5 哈希白/黑名单、Shannon 熵、基于 median/MAD 的稳健 Z 分数与加权威胁评分识别可疑文件；附 4 KB 浏览器端 logistic regression 模型加分。提供交互式 Web 界面（联动图表、筛选排序）。支持 PHP 4.3 至 8，无外部依赖；注意黑名单文件可被自动删除。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- token 匹配 + MD5 黑白名单 + Shannon 熵 + 稳健 Z 分数的组合检测
- 4 KB 浏览器端 logistic regression 模型为威胁评分加分
- 加权威胁评分含 RCE+混淆/上传/用户输入组合乘数与侦察函数规则
- 单 PHP 文件自包含，支持 PHP 4.3–8，无外部依赖

## 适用场景

- 排查 Web 服务器是否被植入 webshell 后门
- 对比文件集统计特征找出异常文件（熵、ctime-mtime 差等）
- 通过 MD5 黑白名单批量清理已知恶意/可信文件

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: PHP web application that scans a directory for PHP and related files and analyses each one for malicious code.
> L18: * **Tiny ML model**: a 4 KB logistic regression over hashed token features, run in the browser. Its score adds poin

## 星数曲线

```mermaid
xychart-beta
    title "Cvar1984/sussyfinder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-31 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `2d5d3ad0a7bc` · [字段定义](../../DATASET.md)*
